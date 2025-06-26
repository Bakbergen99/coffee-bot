from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_dose_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🎛️ <b>Дозировка және рецепт / Дозировка и рецепт</b>\n\n"

        
        "Кофе дайындауда грамм мен миллилитр — дәмнің дәлдігіне жол ашады.\n\n"
        "⚖️ <b>Дозировка:</b>\n"
        "• Эспрессо: 18–20 г кофе → 36–40 г сусын (1:2)\n"
        "• Пуровер: 15–18 г кофе → 250–300 мл су (1:16–1:17)\n"
        "• Фрэнч-пресс: 30 г кофе → 500 мл су\n"
        "• Аэропресс: 14–16 г кофе → 200 мл су\n\n"
        "🧪 <b>Рецепт таңдағанда:</b>\n"
        "• Дәмге сай доза реттеледі\n"
        "• Қаттырақ — доза арттырамыз, жұмсағырақ — азайтамыз\n"
        "• Суды граммен өлшесең — нәтиже тұрақты болады\n\n"
        
        "Граммы и миллилитры — ключ к точному вкусу.\n\n"
        "⚖️ <b>Дозировка:</b>\n"
        "• Эспрессо: 18–20 г кофе → 36–40 г напитка (1:2)\n"
        "• Пуровер: 15–18 г кофе → 250–300 мл воды (1:16–1:17)\n"
        "• Френч-пресс: 30 г кофе → 500 мл воды\n"
        "• Аэропресс: 14–16 г кофе → 200 мл воды\n\n"
        "🧪 <b>Подбор рецепта:</b>\n"
        "• Меняя дозу — регулируем вкус\n"
        "• Больше кофе — крепче, меньше — мягче\n"
        "• Взвешивайте воду — стабильность обеспечена\n\n"
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

dose_info_handler = CallbackQueryHandler(show_dose_info, pattern="^info_dose$")
