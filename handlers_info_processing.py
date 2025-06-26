from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_processing_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🧼 <b>Кофе өңдеу тәсілдері / Способы обработки кофе</b>\n\n"

       
        "Кофе дәндері жемістің ішінен алынады, сондықтан оларды дәмін сақтау үшін арнайы әдіспен өңдейді. Бұл дәм профиліне тікелей әсер етеді.\n\n"
        "1️⃣ <b>Жуылған (Washed / Wet)</b>\n"
        "• Жемістің целлюлозасы толық жуылып алынады\n"
        "• Жуылған кофе — таза, қышқылдығы айқын, балғын дәм\n"
        "• Эфиопия, Колумбияда кең таралған\n\n"
        "2️⃣ <b>Табиғи (Natural / Dry)</b>\n"
        "• Жеміс толықтай кептіріледі, дән ішіне қант сіңеді\n"
        "• Дәмі тәтті, жидекті, күрделі\n"
        "• Эфиопия мен Бразилияда жиі қолданылады\n\n"
        "3️⃣ <b>Honey (Бал әдісі)</b>\n"
        "• Жемістің бір бөлігі ғана қалады (клейковинасы)\n"
        "• Дәмі: бал тəттісі, жұмсақ, майлы, таза\n"
        "• Көбіне Коста-Рикада қолданылады\n\n"
        
        "Кофейные зёрна — это семена ягоды. Чтобы сохранить и развить вкус, их обрабатывают разными способами:\n\n"
        "1️⃣ <b>Мытая (Washed / Wet)</b>\n"
        "• Мякоть ягоды полностью удаляется водой\n"
        "• Вкус: чистый, с выраженной кислотностью\n"
        "• Часто используется в Колумбии, Эфиопии\n\n"
        "2️⃣ <b>Натуральная (Natural / Dry)</b>\n"
        "• Ягода сушится целиком\n"
        "• Вкус: фруктовый, сладкий, насыщенный\n"
        "• Применяется в Бразилии и Эфиопии\n\n"
        "3️⃣ <b>Хани (Honey)</b>\n"
        "• Часть мякоти остаётся на зёрне\n"
        "• Вкус: медовый, маслянистый, мягкий\n"
        "• Популярен в Коста-Рике\n\n"
        "☕ Өңдеу — кофенің тағдыры!"
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

processing_info_handler = CallbackQueryHandler(show_processing_info, pattern="^info_processing$")
