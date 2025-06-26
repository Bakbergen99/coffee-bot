from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ContextTypes



async def show_minigames_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(
    "🏗️ Coffee Tower",
    web_app=WebAppInfo(url="https://bakbergen99.github.io/coffee-tower/")
)
],

        [InlineKeyboardButton("☕ Lucky Cup", callback_data="luckycup_start")],
        [InlineKeyboardButton("⚡ Speed Brew", callback_data="speedbrew_start")],
        [InlineKeyboardButton("🍶 Ингредиент таңдау", callback_data="ingredient_start")],
        [InlineKeyboardButton("🔙 Артқа", callback_data="main_menu")]
    ]

    await update.callback_query.message.edit_text(
        "🎮 Қай ойынды ойнаймыз?",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
