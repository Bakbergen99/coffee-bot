from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_v60_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🫖 <b>V60 әдісімен кофе қайнату</b>\n\n"
        "🔹 V60 — фильтрмен құйылып дайындалатын pour-over әдісі.\n"
        "🔹 Бұл әдісте кофе мен судың тікелей байланысы бар, дәмін айқын сезінуге мүмкіндік береді.\n\n"
        "📋 Құралдар:\n"
        "• V60 дриппер\n• Фильтр қағаз\n• Қайнаған су (90–96°C)\n• Уақталған кофе (18–20 г)\n• Қол таразы\n• Таймер\n\n"
        "📌 Процесс:\n"
        "1. Фильтр қағазды жуып, дрипперге орнат.\n"
        "2. Кофені салып, нөлден баста.\n"
        "3. 30–40 мл су құйып (блуминг), 30 сек күте тұр.\n"
        "4. Суық сумен біртіндеп (айналдырып) 250–300 мл дейін құй.\n"
        "5. Жалпы уақыт 2:30–3:00 мин.\n\n"
        "🎯 Кеңес: Суды ортасынан бастап құйып, шетке қарай айналдыра құй.\n\n"
        "———\n\n"
        "🫖 <b>Приготовление кофе методом V60</b>\n\n"
        "🔹 V60 — это метод pour-over, при котором вода вручную проливается через фильтр с кофе.\n"
        "🔹 Этот способ даёт чистый, яркий вкус и подходит для оценки зерна.\n\n"
        "📋 Что нужно:\n"
        "• Дриппер V60\n• Бумажный фильтр\n• Вода (90–96°C)\n• Кофе (18–20 г)\n• Весы\n• Таймер\n\n"
        "📌 Шаги:\n"
        "1. Промой фильтр и установи его в дриппер.\n"
        "2. Засыпь кофе, обнули весы.\n"
        "3. Налей 30–40 мл воды и подожди 30 секунд (блуминг).\n"
        "4. Постепенно доливай воду круговыми движениями до 250–300 мл.\n"
        "5. Общее время: 2:30–3:00 мин.\n\n"
        "🎯 Совет: Лей воду по центру, затем по кругу к краям."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

v60_handler = CallbackQueryHandler(show_v60_info, pattern="^info_v60$")
