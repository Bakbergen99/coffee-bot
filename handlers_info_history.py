from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, ContextTypes

# ☕ Кофе тарихы
async def show_coffee_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
       "☕ <b>Кофенің тарихы / История кофе</b>\n\n"

        "📍 Барлығы Эфиопиядан басталды. Аңыз бойынша, Калдим есімді шопан ешкілерінің ерекше белсенді болғанын байқайды. "
        "Олар қызыл жемісті жеп, секіріп, ұйықтамай қойған.\n\n"
        "👀 Қызыққан шопан бұл жемісті жақын маңдағы монастырьге апарады. Монахтар одан тұнба жасап, түнгі дұғада ұйықтамау үшін ішкен.\n\n"
        "🌍 Содан кейін кофе Йеменге тарады. Суфийлер оны ұзақ намаз оқу үшін қолданды.\n\n"
        "🇹🇷 Түркияда кофе “қасиетті сусын” деп аталды. Мұнда алғаш рет кофе дайындаудың арнайы тәсілдері пайда болды.\n\n"
        "🇮🇹 Венеция мен Еуропада кофе сәнге айналды. Париж, Лондон, Венада кофеханалар ашылып, ол мәдени орынға айналды.\n\n"
        "🌱 XVIII ғасырда кофе плантациялары Латын Америкасына, Индонезияға, Африкаға тарады. Оны отар елдер өсіріп, Еуропаға жеткізетін болды.\n\n"
        "🚀 XX ғасырда Starbucks пен “Third Wave” қозғалысы кофені өнер мен ғылым деңгейіне көтерді.\n\n"
        "🎨 Бүгінде кофе — жай сусын емес, бұл мәдениет, байланыс, стиль!\n\n"

    
        "📍 Всё началось в Эфиопии. По легенде, пастух по имени Калдим заметил, что его козы стали очень активными после поедания красных ягод.\n\n"
        "👀 Он отнёс ягоды монахам. Те заварили напиток и использовали его, чтобы не засыпать во время ночных молитв.\n\n"
        "🌍 Позже кофе распространился в Йемен. Суфии пили его для бодрости на ночных службах.\n\n"
        "🇹🇷 В Турции кофе считался “священным напитком”. Здесь появились первые методы варки.\n\n"
        "🇮🇹 В Венеции, Париже, Лондоне — кофе стал модой. Открылись кофейни, ставшие центрами культуры.\n\n"
        "🌱 В XVIII веке кофе выращивали в колониях: Бразилия, Индонезия, Африка. Европа потребляла — остальной мир производил.\n\n"
        "🚀 В XX веке Starbucks и “Третья волна” превратили кофе в науку и искусство.\n\n"
        "🎨 Сегодня кофе — это не просто напиток. Это стиль жизни, культура и связь между людьми."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

coffee_history_handler = CallbackQueryHandler(show_coffee_history, pattern="^info_history$")
