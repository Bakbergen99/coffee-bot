from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_flavor_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "📊 <b>Дәм профилі / Вкусовой профиль</b>\n\n"

        
        "Кофенің дәмін сипаттау — өнер. Бұл бариста мен дегустаторларға әртүрлі кофе түрлерін ажыратуға көмектеседі.\n\n"
        "👅 <b>Негізгі дәмдер:</b>\n"
        "• Қышқылдық (Acidity) — жидек, цитрус, жеміс дәмі\n"
        "• Тәттілік (Sweetness) — карамель, бал, шоколад\n"
        "• Ащылық (Bitterness) — қара шоколад, қуыру деңгейі жоғары кофе\n"
        "• Дене (Body) — тығыздық сезімі, ауыр не жеңіл\n"
        "• Афтетейст (Aftertaste) — жұтқаннан кейінгі дәм\n\n"
        "🎨 <b>Дәм дөңгелегі:</b> Кофе индустриясында арнайы дәм дөңгелегі бар (Flavor Wheel), онда жүздеген дәм нотасы бар.\n"
        "Тренировка мен зейін арқылы әр дәмді ажыратуға болады.\n\n"
        
        "Описывать вкус кофе — это искусство. Это помогает бариста и дегустаторам различать сорта и регионы.\n\n"
        "👅 <b>Основные вкусы:</b>\n"
        "• Кислотность (Acidity) — ягоды, цитрус, фрукты\n"
        "• Сладость (Sweetness) — карамель, мед, шоколад\n"
        "• Горечь (Bitterness) — темный шоколад, сильная обжарка\n"
        "• Тело (Body) — ощущение плотности, густоты\n"
        "• Послевкусие (Aftertaste) — вкус после глотка\n\n"
        "🎨 <b>Flavor Wheel:</b> В индустрии кофе используют специальное колесо вкусов с сотнями нот.\n"
        "Тренируйте вкус — и вы услышите всё!\n\n"
        "🧠 Дәмді сезу — тек тіл емес, тәжірибе мен назар!"
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

flavor_info_handler = CallbackQueryHandler(show_flavor_info, pattern="^info_flavor$")
