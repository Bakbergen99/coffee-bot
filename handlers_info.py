from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

# ☕ Кофе дәндері туралы ақпарат
async def show_coffee_beans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
        "🌱 <b>Кофе дәндері / Зерна кофе</b>\n\n"

        
        "Кофе дәні — бұл шын мәнінде жемістің тұқымы. Оның түрі, шыққан аймағы және өңдеу тәсілі кофенің дәміне тікелей әсер етеді.\n\n"
        "🔸 <b>Арабика (Arabica)</b> — ең кең таралған түрі (шамамен 60–70%).\n"
        "• Дәмі — жұмсақ, қышқылдау, хош иісті.\n"
        "• Биіктікте өседі, күтімі қиын.\n"
        "• Эфиопия, Колумбия, Бразилия – негізгі елдер.\n\n"
        "🔸 <b>Робуста (Robusta)</b> — арзанырақ, құрамында кофеині көп.\n"
        "• Дәмі — ащы, күшті, жер дәмі бар.\n"
        "• Төмен биіктікте өседі, төзімді.\n\n"
        "🔸 <b>Liberica & Excelsa</b> — сирек кездеседі.\n"
        "• Хош иісі ерекше, тропикалық, жемісті дәм береді.\n\n"
        "🎯 Кеңес: Кофені таңдағанда тек дән түріне емес, шыққан аймағына, өңделу әдісіне және қуыру деңгейіне де назар аудар!\n\n"

        
        "Кофейное зёрнышко — это семя плода. Вид, регион и способ обработки напрямую влияют на вкус напитка.\n\n"
        "🔸 <b>Арабика (Arabica)</b> — самый распространённый сорт (60–70%).\n"
        "• Вкус — мягкий, кислотный, ароматный.\n"
        "• Растёт на высоте, требует ухода.\n"
        "• Эфиопия, Колумбия, Бразилия — главные страны.\n\n"
        "🔸 <b>Робуста (Robusta)</b> — дешевле, содержит больше кофеина.\n"
        "• Вкус — резкий, горький, землистый.\n"
        "• Растёт в низинах, устойчива к болезням.\n\n"
        "🔸 <b>Liberica & Excelsa</b> — редкие сорта.\n"
        "• Аромат экзотический, фруктово-цветочный.\n\n"
        "🎯 Совет: При выборе обращай внимание не только на вид зёрен, но и на страну происхождения, метод обработки и обжарку!"
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

coffee_beans_handler = CallbackQueryHandler(show_coffee_beans, pattern="^info_beans$")
