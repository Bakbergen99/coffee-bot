import json
import random
import asyncio
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from utils import load_users, save_users

users = load_users()

# Сұрақтар жүктеу
with open("questions_superbaxa.json", "r", encoding="utf-8") as f:
    SUPERBAXA_QUESTIONS = json.load(f)

# 1. Ереже көрсету
async def superbaxa_rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.callback_query.message.delete()
    except:
        pass

    text = (
    
        "📜 <b>Ереже</b>\n\n"
        "🧠 Барлығы — 10 сұрақ\n"
        "⏱ Әр сұраққа жауап беру уақыты — 4 секунд\n"
        "❌ 1 рет қате жіберсең немесе 4 секунд ішінде жауап бермесең — жеңілесің\n"
        "🏆 Дұрыс жауап беріп, барлық сұрақтан өтсең: +200 ұпай және [LEGEND] мәртебесі\n"
        "💀 Жеңілсең: -100 ұпай және 2 сағат бұл режимді қолдана алмайсың\n\n"
        "📜 <b>Правила</b>\n\n"
        "🧠 Всего — 10 вопросов\n"
        "⏱ На каждый вопрос даётся 4 секунды\n"
        "❌ 1 ошибка или если не успеешь за 4 секунды — поражение\n"
        "🏆 Если ответишь на все правильно: +200 баллов и статус [LEGEND]\n"
        "💀 Если проиграешь: -100 баллов и 2 часа не сможешь использовать этот режим"


)


    keyboard = [
        [InlineKeyboardButton("🚀 Старт", callback_data="start_superbaxa")],
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]
    ]

    await update.effective_chat.send_message(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

# 2. Ойынды бастау
async def start_superbaxa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    user = users.get(user_id, {"score": 0})
    if user.get("score", 0) < 500:

        await update.callback_query.answer("❌ Бұл режимге кіру үшін кемінде 500 ұпай қажет!", show_alert=True)
        return

    try:
        await update.callback_query.message.delete()
    except:
        pass

    users[user_id] = users.get(user_id, {
        "score": 0,
        "games_played": 0,
        "last_played": "",
        "blocked_until": None
    })

    context.user_data["superbaxa"] = {
        "questions": SUPERBAXA_QUESTIONS[:10],  # қатармен сұрақтар
        "current": 0,
        "correct": 0
    }

    await send_superbaxa_question(update, context)

# 3. Сұрақ жіберу
async def send_superbaxa_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = context.user_data["superbaxa"]
    q = data["questions"][data["current"]]

    keyboard = [
        [InlineKeyboardButton(q["options"][0], callback_data="sb_answer_0")],
        [InlineKeyboardButton(q["options"][1], callback_data="sb_answer_1")],
        [InlineKeyboardButton(q["options"][2], callback_data="sb_answer_2")],
        [InlineKeyboardButton(q["options"][3], callback_data="sb_answer_3")],
    ]

    text = f"🧠 SuperBaxa {data['current']+1}/10\n\n<b>{q['question']}</b>"

    msg = await update.effective_chat.send_message(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

    context.user_data["superbaxa_msg_id"] = msg.message_id
    context.user_data["answered"] = False

    await asyncio.sleep(4)

    if not context.user_data.get("answered"):
        await msg.edit_text("⏱ Уақыт бітті! / Время вышло!\n\n❌ Сіз ұтылдыңыз.")
        await finish_superbaxa_game(update, context, won=False)

# 4. Жауап өңдеу
async def handle_superbaxa_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = str(update.effective_user.id)

    data = context.user_data.get("superbaxa")
    if not data:
        return

    selected = int(query.data[-1])
    correct = data["questions"][data["current"]]["correct"]

    context.user_data["answered"] = True

    try:
        await query.message.delete()
    except:
        pass

    if selected == correct:
        data["correct"] += 1
        data["current"] += 1
        if data["current"] >= 10:
            await finish_superbaxa_game(update, context, won=True)
        else:
            await send_superbaxa_question(update, context)
    else:
        await update.effective_chat.send_message("❌ Қате жауап! / Неверный ответ!")
        await finish_superbaxa_game(update, context, won=False)

# 5. Ойын аяқтау
async def finish_superbaxa_game(update: Update, context: ContextTypes.DEFAULT_TYPE, won: bool):
    user_id = str(update.effective_user.id)
    user = users.get(user_id, {"score": 0})
    score = user.get("score", 0)

    try:
        msg_id = context.user_data.get("superbaxa_msg_id")
        if msg_id:
            await update.effective_chat.delete_message(msg_id)
    except:
        pass

    if won:
        user["score"] = score + 200
        text = (
            "🏆 <b>Сіз SuperBaxa режимін сәтті аяқтадыңыз!</b>\n\n"
            "+200 ұпай 🎉\n🔥 [LEGEND] мәртебесі берілді!"
        )
    else:
        user["score"] = max(0, score - 100)
        user["blocked_until"] = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
        text = (
            "😢 <b>Сіз SuperBaxa режимінен өте алмадыңыз</b>\n\n"
            "-100 ұпай\n⛔ 2 сағаттық блокировка"
        )

    users[user_id] = user
    save_users(users)

    context.user_data.pop("superbaxa", None)
    context.user_data.pop("answered", None)

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]
    ]

    await update.effective_chat.send_message(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )
