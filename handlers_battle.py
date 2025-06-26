# handlers_battle.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
import random, asyncio, time, json
from utils import load_users, save_users


waiting_player = None
waiting_context = None
active_battles = {}
user_states = {}

with open("questions.json", "r", encoding="utf-8") as f:
    all_questions = json.load(f)

async def battle_rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    text = (
        "⚔️ <b>1x1 Баттл режимі / Режим 1x1 Баттл</b>\n\n"
        "🇰🇿 Екі ойыншы бір-біріне қарсы жарысады. Әрқайсысы жеке сұрақтар алады, бірақ сұрақтар бірдей.\n"
        "⏱️ Уақыт шектеулі: 1 минут.\n"
        "✅ Дұрыс жауап: +10 ұпай\n❌ Қате жауап: -5 ұпай\n"
        "🏆 Кім көп ұпай жинаса — сол жеңімпаз!\n\n"
        "🇷🇺 Два игрока соревнуются друг с другом. Вопросы одинаковые, но ответы даются отдельно.\n"
        "⏱️ Время ограничено: 1 минута.\n"
        "✅ Верный ответ: +10 очков\n❌ Неверный: -5 очков\n"
        "🏆 Побеждает набравший больше баллов.\n"
    )
    keyboard = [[InlineKeyboardButton("🚀 Старт / Start", callback_data="start_battle")],
                [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]]
    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def start_battle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global waiting_player, waiting_context
    user_id = update.callback_query.from_user.id
    await update.callback_query.answer()

    if waiting_player is None:
        waiting_player = user_id
        waiting_context = context
        await update.callback_query.edit_message_text(
            "🕹️ Қарсылас ізделуде...\n\n⏳ Күтіңіз. / Ожидание соперника...",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🛑 Стоп / Остановить", callback_data="cancel_battle")],
                [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]
            ])
        )

    else:
        opponent_id = waiting_player
        opponent_ctx = waiting_context
        waiting_player = None
        waiting_context = None
        await pair_players(user_id, opponent_id, context, opponent_ctx)

async def pair_players(user1_id, user2_id, ctx1, ctx2):
    questions = random.sample(all_questions, min(50, len(all_questions)))

    active_battles[user1_id] = user2_id
    active_battles[user2_id] = user1_id

    user_states[user1_id] = {
        "score": 0, "correct": 0, "wrong": 0, "index": 0,
        "start_time": time.time(), "questions": questions, "last_msg": None
    }
    user_states[user2_id] = {
        "score": 0, "correct": 0, "wrong": 0, "index": 0,
        "start_time": time.time(), "questions": questions, "last_msg": None
    }

    asyncio.create_task(battle_timer(user1_id, ctx1))
    asyncio.create_task(battle_timer(user2_id, ctx2))

    await send_question_to_user(user1_id, ctx1)
    await send_question_to_user(user2_id, ctx2)

async def battle_timer(user_id, context):
    await asyncio.sleep(60)
    if user_id in active_battles:
        opponent_id = active_battles[user_id]
        # 🔒 Тек бір рет ғана finish_battle шақыру
        if user_id < opponent_id:
            await finish_battle(user_id, opponent_id, context)


async def send_question_to_user(user_id, context):
    state = user_states[user_id]
    index = state["index"]

    if index >= len(state["questions"]):
        return

    q = state["questions"][index]
    keyboard = [
        [InlineKeyboardButton(f"1️⃣ {q['options'][0]}", callback_data="battle_ans_0")],
        [InlineKeyboardButton(f"2️⃣ {q['options'][1]}", callback_data="battle_ans_1")],
        [InlineKeyboardButton(f"3️⃣ {q['options'][2]}", callback_data="battle_ans_2")],
        [InlineKeyboardButton(f"4️⃣ {q['options'][3]}", callback_data="battle_ans_3")]
    ]

    text = f"❓ <b>{q.get('question_kz', '')} / {q.get('question_ru', '')}</b>"

    if state.get("last_msg"):
        try:
            await context.bot.edit_message_text(
                chat_id=user_id,
                message_id=state["last_msg"],
                text=text,
                parse_mode="HTML",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return
        except:
            pass

    msg = await context.bot.send_message(
        chat_id=user_id,
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    state["last_msg"] = msg.message_id

async def handle_battle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.callback_query.from_user.id
    if user_id not in user_states:
        return
    state = user_states[user_id]
    q = state["questions"][state["index"]]
    answer_index = int(update.callback_query.data[-1])

    if q["options"][answer_index] == q["correct"]:
        state["score"] += 10
        state["correct"] += 1
    else:
        state["score"] -= 5
        state["wrong"] += 1

    state["index"] += 1
    await update.callback_query.answer()

    # ✅ Соңғы жауап ID сақтау
    state["last_msg"] = update.callback_query.message.message_id

    await send_question_to_user(user_id, context)

async def finish_battle(user1_id, user2_id, context):
    if user1_id not in active_battles or user2_id not in active_battles:
        return

    for uid in [user1_id, user2_id]:
        msg_id = user_states.get(uid, {}).get("last_msg")
        if msg_id:
            try:
                await context.bot.delete_message(chat_id=uid, message_id=msg_id)
            except:
                pass

    for uid in [user1_id, user2_id]:
        my_data = user_states.get(uid, {})
        op_id = user1_id if uid == user2_id else user2_id
        op_data = user_states.get(op_id, {})

        result = (
            f"📊 <b>Нәтиже / Результат</b>\n\n"
            f"👤 <b>Сіз:</b> {my_data.get('score', 0)} ұпай\n"
            f"• Дұрыс: {my_data.get('correct', 0)} / Қате: {my_data.get('wrong', 0)}\n"
            f"• Сұрақтар саны: {my_data.get('index', 0)}\n\n"
            f"👥 <b>Қарсылас:</b> {op_data.get('score', 0)} ұпай\n"
            f"• Дұрыс: {op_data.get('correct', 0)} / Қате: {op_data.get('wrong', 0)}\n"
            f"• Сұрақтар саны: {op_data.get('index', 0)}\n\n"
        )

        if my_data.get('score', 0) > op_data.get('score', 0):
            result += "🎉 <b>Сіз жеңдіңіз! / Вы победили!</b>"
        elif my_data.get('score', 0) < op_data.get('score', 0):
            result += "😬 <b>Сіз жеңілдіңіз / Вы проиграли</b>"
        else:
            result += "✌️ <b>Тең ойын / Ничья</b>"

        keyboard = [
            [InlineKeyboardButton("🔁 Қайта ойнау / Играть снова", callback_data="start_battle")],
            [InlineKeyboardButton("🏠 Басты мәзір / Главное меню", callback_data="main_menu")]
        ]

        await context.bot.send_message(
            chat_id=uid,
            text=result,
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # ✅ Статистика сақтау
    users = load_users()
    for uid in [user1_id, user2_id]:
        data = user_states.get(uid, {})
        user = users.get(str(uid), {
            "name": "Аноним",
            "score": 0,
            "games_played": 0,
            "last_mode": ""
        })

        user["score"] += data.get("score", 0)
        user["games_played"] += 1
        user["last_mode"] = "1x1"
        users[str(uid)] = user
    save_users(users)

    for uid in [user1_id, user2_id]:
        active_battles.pop(uid, None)
        user_states.pop(uid, None)



async def cancel_battle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global waiting_player, waiting_context
    user_id = update.callback_query.from_user.id

    if waiting_player == user_id:
        waiting_player = None
        waiting_context = None
        await update.callback_query.edit_message_text(
            "❌ Іздеу тоқтатылды / Поиск отменён.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Басты мәзір / Главное меню", callback_data="main_menu")]
            ])
        )
    else:
        await update.callback_query.answer("❌ Сіз күтуде емессіз. / Вы не в очереди.", show_alert=True)

