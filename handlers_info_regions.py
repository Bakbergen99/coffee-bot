from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_regions_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🌍 <b>Елдер мен аймақтардағы кофе дәмі / Вкусовые особенности по регионам</b>\n\n"

       
        "Кофенің дәмі оның қай жерде өсірілгеніне байланысты өзгереді. Әр аймақтың климаты, топырағы мен өңдеу тәсілдері ерекше профиль қалыптастырады:\n\n"
        "🇪🇹 <b>Эфиопия:</b>\n"
        "• Жидек дәмі, гүлді ноталар, жеңіл қышқылдық\n"
        "• Қолмен терілген, табиғи және жуылған әдістер кең таралған\n\n"
        "🇨🇴 <b>Колумбия:</b>\n"
        "• Теңгерімді, жаңғақ, шоколад, цитрус дәмі\n"
        "• Негізінен жуылған әдіс қолданылады\n\n"
        "🇧🇷 <b>Бразилия:</b>\n"
        "• Ащы-тәтті, жаңғақ, какао, ауыр денелі\n"
        "• Табиғи және Honey әдісі кеңінен қолданылады\n\n"
        "🇰🇪 <b>Кения:</b>\n"
        "• Ашық қышқыл, жидек, қызанақ ноталары\n"
        "• Әдетте жуылған әдіс\n\n"
        "🇮🇩 <b>Индонезия:</b>\n"
        "• Жер дәмі, дәмдеуіш, ауыр дене\n"
        "• Гүлді және шөпті нюанстар\n\n"
        
        "Вкус кофе сильно зависит от региона произрастания. Вот примеры:\n\n"
        "🇪🇹 <b>Эфиопия:</b>\n"
        "• Ягодный, цветочный, лёгкая кислотность\n"
        "• Чаще натуральная и мытая обработка\n\n"
        "🇨🇴 <b>Колумбия:</b>\n"
        "• Баланс, орех, шоколад, цитрус\n"
        "• Преимущественно мытая обработка\n\n"
        "🇧🇷 <b>Бразилия:</b>\n"
        "• Орех, какао, плотное тело\n"
        "• Натуральный и honey методы\n\n"
        "🇰🇪 <b>Кения:</b>\n"
        "• Яркая кислотность, ягоды, томат\n"
        "• Мытая обработка\n\n"
        "🇮🇩 <b>Индонезия:</b>\n"
        "• Землистый, пряный, тяжёлое тело\n"
        "• Часто полумытая обработка (wet-hulled)\n\n"
        "🌱 Әр аймақ — жеке әлем!"
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

regions_info_handler = CallbackQueryHandler(show_regions_info, pattern="^info_regions$")
