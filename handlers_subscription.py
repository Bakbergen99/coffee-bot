# handlers_subscription.py
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from check_subscription import is_user_subscribed
from handlers_menu import show_inline_main_menu

async def handle_check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    if await is_user_subscribed(bot, user_id):
        await update.callback_query.message.edit_text(
            text="✅ Сіз арнаға тіркелдіңіз!\nМенюге өтейік:"
        )
        await show_inline_main_menu(update, context)
    else:
        await update.callback_query.answer("❗️Сіз әлі тіркелмегенсіз!", show_alert=True)
