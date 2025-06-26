from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def feedback_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = (
        "✉️ <b>Кері байланыс / Обратная связь</b>\n\n"
        "Ұсыныстарыңыз немесе сұрақтарыңыз болса, Telegram арқылы хабарласыңыз:\n"
        '<a href="https://t.me/gtsupra">@gtsupra</a>'
    )
    
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )
