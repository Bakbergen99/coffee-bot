import json
import random
import asyncio
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes
from utils import load_users, save_users
from handlers_menu import show_inline_main_menu
from telegram.error import BadRequest # Import BadRequest for error handling

# Сұрақтар
with open("questions.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

async def quiz_rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📘 *Кәдімгі викторина ережесі / Правила викторины*\n\n"
        "⏱ 1 сағат ішінде 15 сұраққа жауап беріңіз.\n"
        "📌 12+ дұрыс жауап — 70 ұпай\n"
        "📌 8-11 дұрыс жауап — 40 ұпай\n"
        "📌 7 немесе аз — қатысқаны үшін 30 ұпай\n\n"
        "👇 Бастау үшін 'Старт' батырмасын басыңыз:"
    )

    keyboard = [
        [InlineKeyboardButton("🚀 Старт", callback_data="start_quiz")],
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="back_to_menu")]
    ]
    markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=markup)
    elif update.callback_query:
        try:
            await update.callback_query.message.edit_text(text, parse_mode="Markdown", reply_markup=markup)
        except BadRequest:
            # If message is not modified or other BadRequest occurs, send a new message
            await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=markup)

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    context.user_data["quiz_mode"] = True
    context.user_data["correct_count"] = 0
    context.user_data["wrong_count"] = 0
    context.user_data["question_index"] = 0
    context.user_data["questions"] = random.sample(QUESTIONS, k=15)
    context.user_data["finished"] = False

    await send_quiz_question(update, context)
    asyncio.create_task(end_quiz_timeout(update, context))

async def send_quiz_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    index = context.user_data.get("question_index", 0)
    questions = context.user_data.get("questions", [])

    if index >= len(questions):
        context.user_data["finished"] = True
        await show_quiz_results(update, context)
        return

    question = questions[index]
    options = question["options"].copy()
    random.shuffle(options)

    # Use .get() for robustness, though questions.json is now corrected to have "correct"
    context.user_data["correct_answer"] = question.get("correct")
    context.user_data["question_index"] = index + 1

    text = f"*{question.get('question_kz', 'Вопрос на казахском не найден')}*\n_{question.get('question_ru', 'Вопрос на русском не найден')}_"
    buttons = [[InlineKeyboardButton(opt, callback_data=opt)] for opt in options]
    markup = InlineKeyboardMarkup(buttons)

    if update.callback_query:
        try:
            await update.callback_query.message.edit_text(text, parse_mode="Markdown", reply_markup=markup)
        except BadRequest:
            # If message is not modified or other BadRequest occurs, send a new message
            await update.callback_query.message.reply_text(text, parse_mode="Markdown", reply_markup=markup)
    else:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=markup)

async def handle_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "quiz_stop":
        context.user_data["finished"] = True
        try:
            await query.message.delete()
        except BadRequest:
            pass # Ignore if message already deleted or not found
        await show_inline_main_menu(update, context)
        return

    # More robust check for quiz state to prevent KeyError if context.user_data is incomplete
    # This covers scenarios where bot restarted or an old button is pressed
    if context.user_data.get("finished") or \
       "quiz_mode" not in context.user_data or \
       context.user_data.get("quiz_mode") is False or \
       "correct_answer" not in context.user_data:
        # If the quiz state is invalid, show main menu and return
        # Optionally, you could also send a message like "Викторина уже завершена или некорректна."
        await show_inline_main_menu(update, context)
        return

    # Safely increment counters using .get() with a default value
    if query.data == context.user_data.get("correct_answer"):
        context.user_data["correct_count"] = context.user_data.get("correct_count", 0) + 1
    else:
        context.user_data["wrong_count"] = context.user_data.get("wrong_count", 0) + 1

    await send_quiz_question(update, context)

async def end_quiz_timeout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await asyncio.sleep(3600)  # 1 сағат
    if not context.user_data.get("finished"):
        context.user_data["finished"] = True
        await show_quiz_results(update, context)

async def show_quiz_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    correct = context.user_data.get("correct_count", 0)
    wrong = context.user_data.get("wrong_count", 0)
    total = correct + wrong

    if correct >= 12:
        earned = 70
        title = "☕ Кофе-эксперт"
    elif correct >= 8:
        earned = 40
        title = "🍫 Кофе-әуесқой"
    else:
        earned = 30
        title = "🌱 Жаңадан бастаушы"

    user_id = str(update.effective_user.id)
    users = load_users()
    if user_id not in users:
        users[user_id] = {"name": update.effective_user.first_name or "Аноним", "score": 0}
    users[user_id]["score"] += earned
    save_users(users)

    result = (
        f"🏁 *Викторина аяқталды / Викторина завершена!*\n"
        f"✅ Дұрыс жауап: *{correct}*\n"
        f"❌ Қате жауап: *{wrong}*\n"
        f"📊 Барлығы: *{total}*\n"
        f"🎖 Ұпай: *{earned}*\n"
        f"🏅 Дәреже: *{title}*"
    )

    keyboard = [[InlineKeyboardButton("🔙 Артқа / Назад", callback_data="back_to_menu")]]
    # Use reply_text here, as the previous message might have been deleted by handle_quiz_answer's quiz_stop
    # or the result should be a fresh message.
    try:
        await update.callback_query.message.reply_text(result, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    except Exception as e:
        # Fallback if reply_text fails for some reason
        await update.effective_chat.send_message(result, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))