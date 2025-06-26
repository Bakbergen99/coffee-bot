from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

# ⚙️ Дұрыс помол туралы ақпарат
async def show_coffee_grind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "⚙️ <b>Дұрыс ұнтақтау / Правильный помол</b>\n\n"
        "Кофенің ұнтақталуы — дәмге тікелей әсер ететін фактор.\n\n"
        "• 🟤 Ірі помол — French Press, Cold Brew.\n"
        "• 🟠 Орташа — V60, Chemex.\n"
        "• 🔵 Ұсақ — Эспрессо, Moka Pot.\n\n"
        "Дұрыс помол:\n"
        "• Дәмді теңгерімді етеді\n"
        "• Экстракцияны реттейді\n"
        "• Тым ірі — дәмсіз,қышқыл, әлсіз кофе\n"
        "• Тым ұсақ — ашы, ащы кофе\n\n"
        "🎯 Кеңес: Помолды қолмен реттей алатын кофемолка қолданыңыз."


        "⚙️ <b>Правильный помол кофе</b>\n\n"
        "Помол — один из главных факторов, влияющих на вкус кофе.\n\n"
        "• 🟤 Крупный — для French Press, Cold Brew\n"
        "• 🟠 Средний — для V60, Chemex\n"
        "• 🔵 Мелкий — для Эспрессо, Moka Pot\n\n"
        "Правильный помол:\n"
        "• Делает вкус сбалансированным\n"
        "• Контролирует экстракцию\n"
        "• Слишком крупный — водянистый, кислый вкус\n"
        "• Слишком мелкий — горечь и передозировка\n\n"
        "🎯 Совет: Используйте кофемолку с регулировкой помола."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

coffee_grind_handler = CallbackQueryHandler(show_coffee_grind, pattern="^info_grind$")
