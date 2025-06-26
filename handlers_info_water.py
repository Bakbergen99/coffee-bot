from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_water_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🌡️ <b>Су температурасы және сапасы / Температура и качество воды</b>\n\n"

        
        "Су — кофенің 98% бөлігін құрайды. Сондықтан су сапасы мен температурасы өте маңызды!\n\n"
        "🔥 <b>Температура:</b>\n"
        "• Идеал аралығы: 90°C - 96°C\n"
        "• Тым ыстық су — ащы дәм береді\n"
        "• Тым салқын су — дәм толық ашылмайды\n"
        "• Қайнаған суды 30-60 секунд суытып қолданыңыз\n\n"
        "💧 <b>Су сапасы:</b>\n"
        "• Таза, хлорсыз су қолдану керек\n"
        "• Минерал деңгейі: 75-175 ppm\n"
        "• Арнайы фильтр немесе бөтелке су ұсынылады\n\n"
        "☝️ Есте сақтаңыз: нашар су — ең жақсы кофені де бүлдіреді.\n\n"

        
        "Вода составляет 98% кофе. Поэтому её качество и температура критично важны!\n\n"
        "🔥 <b>Температура воды:</b>\n"
        "• Идеальный диапазон: 90°C - 96°C\n"
        "• Слишком горячая — горечь\n"
        "• Слишком холодная — недоэкстракция\n"
        "• Кипяток остудите 30–60 секунд перед завариванием\n\n"
        "💧 <b>Качество воды:</b>\n"
        "• Используйте чистую воду без хлора\n"
        "• Минерализация: 75-175 ppm\n"
        "• Фильтрованная или бутилированная вода — лучшее решение\n\n"
        "☝️ Помните: плохая вода испортит даже лучший кофе."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

water_info_handler = CallbackQueryHandler(show_water_info, pattern="^info_water$")
