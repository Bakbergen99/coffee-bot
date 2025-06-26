from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from utils import load_users

async def user_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    users = load_users()

    user_data = users.get(user_id)

    if not user_data:
        text = (
            "🚫 Сіз әлі бірде-бір ойын ойнамағансыз.\n"
            "🚫 Вы еще не сыграли ни одной игры.\n\n"
            "Алдымен викторина немесе басқа режимдерді қолданып көріңіз.\n"
            "Сначала попробуйте викторину или другой режим."
        )
    else:
        name = user_data.get("name", "Аты белгісіз / Имя неизвестно")
        score = user_data.get("score", 0)
        games = user_data.get("games_played", 0)
        last_mode = user_data.get("last_mode", "Белгісіз / Неизвестен")

        # 👇 Статус логикасы тікелей ішінде:
        if score >= 4000:
            status = "🥇 Аңыз / Легенда"
        elif score >= 3000:
            status = "🧠 Шебер / Мастер"
        elif score >= 2000:
            status = "🔥 Маманданған / Профи"
        elif score >= 1000:
            status = "🚀 Алға басушы / Продвинутый"
        else:
            status = "🍼 Жаңадан бастаушы / Новичок"

        text = (
            f"👤 <b>Мен туралы / Обо мне</b>\n\n"
            f"🆔 Атыңыз / Имя: <b>{name}</b>\n"
            f"🎯 Жалпы ойын саны / Кол-во игр: <b>{games}</b>\n"
            f"🎮 Соңғы режим / Последний режим: <b>{last_mode}</b>\n"
            f"🏆 Қазіргі ұпай / Текущий рейтинг: <b>{score}</b>\n"
            f"🥇 Мәртебе / Статус: <b>{status}</b>"
        )

    keyboard = [[InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
