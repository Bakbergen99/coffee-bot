from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_aeropress_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🚀 <b>Aeropress әдісімен кофе дайындау</b>\n\n"
        "🔹 Aeropress — қысым арқылы кофе дайындайтын портативті құрылғы.\n"
        "🔹 Бұл әдіс эспрессо мен фильтр кофе арасындағы дәм береді.\n\n"
        "📋 Қажетті құралдар:\n"
        "• Aeropress құрылғысы\n• Фильтр қағаз\n• 14–18 г кофе\n• 200–220 мл су (80–90°C)\n• Таймер\n• Араластыру таяқшасы\n\n"
        "📌 Процесс:\n"
        "1. Фильтрді жуып, қондырғыға орнат.\n"
        "2. Кофені салып, 50 мл су құй — араластыр (блуминг).\n"
        "3. 30 сек күтіп, қалған суды құйып, 1:30–2:00 мин ішінде басып шығар.\n"
        "4. Жоғарғы қысыммен басып шығару керек.\n\n"
        "🎯 Кеңес: Керісінше әдісті (inverted method) де қолданып көр — дәмі өзгеше болуы мүмкін.\n\n"
        "———\n\n"
        "🚀 <b>Приготовление кофе с помощью Aeropress</b>\n\n"
        "🔹 Aeropress — портативное устройство, использующее давление для заваривания.\n"
        "🔹 Вкус — нечто среднее между эспрессо и фильтром.\n\n"
        "📋 Что нужно:\n"
        "• Устройство Aeropress\n• Бумажный фильтр\n• 14–18 г кофе\n• 200–220 мл воды (80–90°C)\n• Таймер\n• Палочка для перемешивания\n\n"
        "📌 Шаги:\n"
        "1. Промой фильтр и установи его в устройство.\n"
        "2. Засыпь кофе, залей 50 мл воды и размешай (блуминг).\n"
        "3. Подожди 30 сек, долей воду, и через 1:30–2:00 мин нажми.\n"
        "4. Прессуй уверенно и стабильно.\n\n"
        "🎯 Совет: Попробуй также перевернутый способ (inverted) — вкус может удивить!"
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

aeropress_handler = CallbackQueryHandler(show_aeropress_info, pattern="^info_aeropress$")
