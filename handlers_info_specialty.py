from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_specialty_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🌟 <b>Specialty кофе деген не? / Что такое Specialty кофе?</b>\n\n"

        "Specialty кофе — бұл сапаның ең жоғарғы деңгейіне жеткен кофе. Ол дәннің сапасынан бастап, фермердің еңбегінен, "
        "баристаның шеберлігіне дейінгі барлық кезеңдерде ерекше көңіл бөлінетін өнім.\n\n"
        "📊 <b>Q-Grader бағасы:</b>\n"
        "Кофе арнайы Q-Grader сарапшыларымен 100 баллдық шкала бойынша бағаланады:\n\n"
        "• 90–100 балл: Керемет (Outstanding)\n"
        "• 85–89.99 балл: Тамаша (Excellent)\n"
        "• 80–84.99 балл: Жақсы (Very Good)\n"
        "• 80-нен төмен: Оңай кофе (коммерциялық деңгей)\n\n"
        "✅ Specialty кофе болуы үшін — кем дегенде 80 балл алу керек!\n\n"
        "🔍 <b>Негізгі шарттар:</b>\n"
        "• Жоғары сапалы арабика сорты\n"
        "• Фермерлік бақылау, экологиялық өңдеу\n"
        "• Дұрыс сақтау және қуыру\n"
        "• Баристаның дәл дайындауы\n\n"
        "☕ Specialty кофе дәмі күрделі, таза, балансты, ерекше ноталармен болады.\n"
        "Бұл — өнер мен ғылымның түйіскен нүктесі!\n\n"

        
        "Specialty кофе — это кофе высочайшего качества, который получает от 80 до 100 баллов по шкале SCA (Specialty Coffee Association). "
        "Оценка проводится профессиональными Q-Grader специалистами.\n\n"
        "📊 <b>Оценочная шкала:</b>\n"
        "• 90–100 баллов: Выдающийся (Outstanding)\n"
        "• 85–89.99 баллов: Отличный (Excellent)\n"
        "• 80–84.99 баллов: Очень хороший (Very Good)\n"
        "• Ниже 80: Обычный коммерческий кофе\n\n"
        "✅ Чтобы называться Specialty, кофе должен получить минимум 80 баллов и пройти строгий контроль на каждом этапе: "
        "от выращивания и обработки до обжарки и заваривания.\n\n"
        "🔍 <b>Требования:</b>\n"
        "• 100% Арабика\n"
        "• Чистота зерна, отсутствие дефектов\n"
        "• Прозрачное происхождение и стабильная логистика\n"
        "• Профессиональное приготовление бариста\n\n"
        "☕ Вкусовой профиль: сложный, чистый, сбалансированный, с яркими нотами (ягоды, цветы, специи и т.д.)\n\n"
        "🌱 Specialty — это уважение к природе, фермеру и культуре кофе."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

specialty_info_handler = CallbackQueryHandler(show_specialty_info, pattern="^info_specialty$")
