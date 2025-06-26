from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils import load_users

async def show_ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = load_users()

    # SuperBaxa қосу
    users["SuperBaxa"] = {
        "name": "🔥 SuperBaxa",
        "score": 10000,
        "games_played": 999,
        "last_played": "∞"
    }

    sorted_users = sorted(users.items(), key=lambda x: x[1]['score'], reverse=True)
    top_users = sorted_users[:10]

    text = "🏆 *Топ 10 рейтинг / Топ 10 рейтинг:*\n\n"
    for i, (user_id, data) in enumerate(top_users, start=1):
        name = data.get("name", f"ID:{user_id}")
        score = data["score"]
        text += f"{i}. {name} — {score} ұпай\n"

    # 🔙 Артқа батырмасы
    keyboard = [[InlineKeyboardButton("🔙 Артқа / Назад", callback_data="back_to_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.callback_query:
        await update.callback_query.answer()
        current_text = update.callback_query.message.text

        # ✅ Хабарлама өзгерген болса ғана edit_text қолдану
        if current_text != text:
            await update.callback_query.message.edit_text(
                text, parse_mode="Markdown", reply_markup=reply_markup
            )
    else:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=reply_markup)
