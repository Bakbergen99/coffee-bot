from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

async def show_espresso_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "⚡ <b>Эспрессо / Espresso әдісі</b>\n\n"
        "🔹 Эспрессо — жоғары қысыммен жасалатын концентрленген кофе. Бұл сусын көптеген басқа кофелердің негізі.\n"
        "🔹 Дұрыс эспрессо — кремалы, теңгерімді, денелі және қышқыл/ащы дәмдер үйлесімді болады.\n\n"
        "📋 Қажетті құралдар:\n"
        "• Эспрессо-машина\n• 18–20 г кофе (fine помол)\n• Тампер\n• Кофемолка\n\n"
        "📌 Процесс:\n"
        "1. Машинаны қыздыр (машина мен портафильтр жылы болуы керек).\n"
        "2. 18–20 г кофе сал, тегістеп тампермен нығызда.\n"
        "3. Эспрессоны іске қос — 25–30 секунд ішінде 36–40 мл шығуы тиіс.\n"
        "4. Егер дәмі тым ащы болса — ұнтақты ірілеу жаса. Егер қышқыл болса — ұнтақты ұсақта.\n\n"
        "🎯 Кеңес: Кофе мен судың арақатынасы — 1:2 (мысалы, 18 г кофе → 36 г сұйықтық).\n\n"
        "———\n\n"
        "⚡ <b>Espresso метод</b>\n\n"
        "🔹 Эспрессо — концентрированный кофе, приготовленный под высоким давлением. Основа для многих напитков.\n"
        "🔹 Идеальный шот — с хорошей кремой, сбалансированный по кислотности и горечи.\n\n"
        "📋 Что нужно:\n"
        "• Эспрессо-машина\n• 18–20 г кофе (мелкий помол)\n• Темпер\n• Кофемолка\n\n"
        "📌 Шаги:\n"
        "1. Разогрей машину и группу.\n"
        "2. Засыпь 18–20 г кофе, утрамбуй темпером.\n"
        "3. Запусти заваривание — за 25–30 сек должно выйти 36–40 мл.\n"
        "4. Горько? — грубее. Кисло? — мельче помол.\n\n"
        "🎯 Совет: Соотношение — 1:2 (например, 18 г кофе → 36 г напитка)."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

espresso_handler = CallbackQueryHandler(show_espresso_info, pattern="^info_espresso$")
