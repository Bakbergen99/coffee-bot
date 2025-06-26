from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
import json
import random
import asyncio
from utils import load_users, save_users
from handlers_menu import show_inline_main_menu

# Сұрақтарды жүктеу
with open("questions.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

# Соло режим ережесі
async def solo_rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🧍‍♂️ *Соло режимінің ережесі*\n\n"
        "⏱ *60 секунд ішінде* мүмкіндігінше көп сұраққа жауап беріңіз.\n"
        "✅ Әр дұрыс жауап — *+10 ұпай*\n"
        "❌ Әр қате жауап — *-5 ұпай*\n\n"
        "🧍‍♂️ *Правила соло режима*\n\n"
        "⏱ *В течение 60 секунд* ответьте на как можно больше вопросов.\n"
        "✅ Каждый правильный ответ — *+10 баллов*\n"
        "❌ Каждый неправильный ответ — *-5 баллов*\n\n"
        "👇 Жауап нұсқасын таңдаңыз / Выберите вариант ответа:"
    )
    keyboard = [
        [InlineKeyboardButton("🚀 Старт", callback_data="start_solo")],
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="back_to_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.edit_text(text, parse_mode="Markdown", reply_markup=reply_markup)

# Ойынды бастау
async def start_solo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data.update({
        "score": 0,
        "correct_answers": 0,
        "wrong_answers": 0,
        "total_questions": 0,
        "start_time": asyncio.get_event_loop().time(),
        "finished": False,
        "questions": random.sample(QUESTIONS, k=len(QUESTIONS)),
        "question_index": 0,
    })

    await send_question(update, context)
    asyncio.create_task(end_game_after_timeout(update, context))

# Сұрақты жіберу
async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("finished"):
        return

    index = context.user_data["question_index"]
    questions = context.user_data["questions"]

    if index >= len(questions):
        context.user_data["finished"] = True
        await show_solo_results(update, context)
        return

    question = questions[index]
    options = question["options"].copy()
    random.shuffle(options)
    correct = question["correct"]
    correct_index = options.index(correct)

    context.user_data["correct_index"] = correct_index
    context.user_data["question_index"] = index + 1
    context.user_data["total_questions"] += 1

    text = f"*{question.get('question_kz', '')}*\n_{question.get('question_ru', '')}_"
    # Мәтін бос болмасын
    if not text.strip():
        text = "❌ Сұрақ мәтіні бос. / Вопрос пустой."
    buttons = [[InlineKeyboardButton(opt, callback_data=str(i))] for i, opt in enumerate(options)]
    reply_markup = InlineKeyboardMarkup(buttons)

    message = update.callback_query.message if update.callback_query else update.message
    message = update.callback_query.message if update.callback_query else update.message

    msg = await message.edit_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

    context.user_data["last_msg"] = msg.message_id



# Жауапты өңдеу
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data in ["back", "back_to_menu"]:
        msg_id = context.user_data.get("last_msg")
        if msg_id:
            try:
                await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=msg_id)
            except:
                pass
        context.user_data["last_msg"] = None

        await query.message.delete()
        await show_inline_main_menu(update, context)
        return

    if query.data == "start_solo":
        await start_solo(update, context)
        return

    if query.data == "restart_solo":
        msg_id = context.user_data.get("last_msg")
        if msg_id:
            try:
                await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=msg_id)
            except:
                pass
            context.user_data["last_msg"] = None

        await start_solo(update, context)
        return

    if context.user_data.get("finished"):
        return

    try:
        selected = int(query.data)
    except ValueError:
        return

    if selected == context.user_data.get("correct_index"):
        context.user_data["score"] += 10
        context.user_data["correct_answers"] += 1
    else:
        context.user_data["score"] -= 5
        context.user_data["wrong_answers"] += 1

    now = asyncio.get_event_loop().time()
    if now - context.user_data["start_time"] >= 60:
        context.user_data["finished"] = True
        await show_solo_results(update, context)
    else:
        await send_question(update, context)

# 60 секундтан кейін аяқтау
async def end_game_after_timeout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await asyncio.sleep(60)
    if not context.user_data.get("finished"):
        context.user_data["finished"] = True
        await show_solo_results(update, context)



# Нәтижені көрсету
async def show_solo_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    score = context.user_data["score"]
    correct = context.user_data["correct_answers"]
    wrong = context.user_data["wrong_answers"]
    total = correct + wrong

    text = (
        f"🏁 *Ойын аяқталды / Игра окончена!*\n\n"
        f"✅ Дұрыс жауап / Верных: *{correct}*\n"
        f"❌ Қате жауап / Ошибок: *{wrong}*\n"
        f"❓ Барлығы / Всего: *{total}* сұрақ\n"
        f"🧠 Ұпай / Баллы: *{score}*"
    )

    user_id = str(update.effective_user.id)
    user_name = update.effective_user.first_name or "Аноним"
    users = load_users()


    if user_id not in users:
        users[user_id] = {
            "name": user_name,
            "score": 0,
            "games_played": 0,
            "last_mode": ""
        }

    users[user_id]["score"] += score
    users[user_id]["games_played"] += 1
    users[user_id]["last_mode"] = "Соло"

    save_users(users)

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔁 Қайта ойнау / Рестарт", callback_data="restart_solo")],
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="back")]
    ])

    await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=buttons)
