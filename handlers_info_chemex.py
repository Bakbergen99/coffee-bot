from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_chemex_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🧪 <b>Chemex әдісімен кофе дайындау</b>\n\n"
        "🔹 Chemex — стильді және классикалық pour-over әдісі.\n"
        "🔹 Қалың фильтр, әйнек ыдыс арқылы кофе жұмсақ әрі таза дәм береді.\n\n"
        "📋 Қажетті құралдар:\n"
        "• Chemex ыдысы\n• Арнайы қалың фильтр\n• 40–50 г кофе\n• 600–700 мл су\n• Таразы\n• Таймер\n\n"
        "📌 Қадамдар:\n"
        "1. Фильтрді жуып, ыдысқа орнат.\n"
        "2. Кофені салып, 60–70 мл су құй (блуминг).\n"
        "3. 30–40 секунд күтіп, сумен біртіндеп айналдыра құй.\n"
        "4. Жалпы су көлемі 600 мл шамасында болуы керек.\n"
        "5. Дайын болу уақыты – 4:00–5:00 минут.\n\n"
        "🎯 Кеңес: Chemex фильтрі қалың болғандықтан, қайнату уақыты сәл ұзағырақ болады.\n\n"
        "———\n\n"
        "🧪 <b>Приготовление кофе в Chemex</b>\n\n"
        "🔹 Chemex — классический стильный pour-over метод.\n"
        "🔹 Благодаря толстому фильтру и стеклянной колбе, вкус получается мягким и чистым.\n\n"
        "📋 Что нужно:\n"
        "• Колба Chemex\n• Фирменный бумажный фильтр\n• 40–50 г кофе\n• 600–700 мл воды\n• Весы\n• Таймер\n\n"
        "📌 Шаги:\n"
        "1. Промой фильтр и установи его в Chemex.\n"
        "2. Засыпь кофе, влей 60–70 мл воды (блуминг).\n"
        "3. Подожди 30–40 сек и продолжай заливку по кругу.\n"
        "4. Объем воды — около 600 мл.\n"
        "5. Время приготовления: 4:00–5:00 минут.\n\n"
        "🎯 Совет: Из-за толщины фильтра процесс немного медленнее."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

chemex_handler = CallbackQueryHandler(show_chemex_info, pattern="^info_chemex$")
