from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_frenchpress_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🫙 <b>French Press әдісімен кофе дайындау</b>\n\n"
        "🔹 French Press — ең қарапайым әрі танымал әдістердің бірі.\n"
        "🔹 Қайнату тікелей су ішінде жүреді, сондықтан денелі, бай дәм шығады.\n\n"
        "📋 Қажетті құралдар:\n"
        "• French Press\n• 18–20 г кофе (ірі ұнтақталған)\n• 300–350 мл су (92–96°C)\n• Таймер\n• Қасық\n\n"
        "📌 Қадамдар:\n"
        "1. Кофені ыдысқа сал.\n"
        "2. 50 мл су құйып, 30 секунд демде (блуминг).\n"
        "3. Қалған суды қосып, 4:00 мин күте тұрып, қасықпен көбікті алыңыз.\n"
        "4. Поршеньді ақырын басып, кофе дайын!\n\n"
        "🎯 Кеңес: French Press-та сүзгі болмайтындықтан, соңғы 10 мл ішпеуге кеңес беріледі.\n\n"
        "———\n\n"
        "🫙 <b>Приготовление кофе во French Press</b>\n\n"
        "🔹 French Press — один из самых простых и популярных способов.\n"
        "🔹 Заваривание происходит прямо в воде, вкус получается насыщенным.\n\n"
        "📋 Что нужно:\n"
        "• French Press\n• 18–20 г кофе (крупный помол)\n• 300–350 мл воды (92–96°C)\n• Таймер\n• Ложка\n\n"
        "📌 Шаги:\n"
        "1. Засыпьте кофе в колбу.\n"
        "2. Влейте 50 мл воды, дайте настояться 30 секунд (блуминг).\n"
        "3. Долейте оставшуюся воду и подождите 4:00 минуты.\n"
        "4. Снимите пенку ложкой и нажмите поршень — готово!\n\n"
        "🎯 Совет: последние миллилитры лучше не пить — там может быть гуща."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

frenchpress_handler = CallbackQueryHandler(show_frenchpress_info, pattern="^info_frenchpress$")
