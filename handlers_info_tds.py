from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

# 📐 TDS және экстракция туралы
async def show_coffee_tds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    text = (
       "📐 <b>TDS және экстракция</b>\n\n"
"TDS — Total Dissolved Solids (еріген заттардың жалпы мөлшері), яғни кофенің дәмін құрайтын еріген бөліктер.\n\n"
"• TDS пайызбен өлшенеді (мысалы, 1.30–1.50%)\n"
"• Экстракция — кофе дәнінен қаншалықты зат алынғаны (18–22% идеал)\n\n"
"Экстракцияға әсер ететіндер:\n"
"• Помол өлшемі\n"
"• Температура\n"
"• Қайнату уақыты\n"
"• Судың сапасы\n\n"
"🎯 Кеңес: Экстракция тым аз болса — дәмсіз, қышқыл болады, тым көп болса — ащы дәм шығады."


"📐 <b>TDS и экстракция</b>\n\n"
"TDS — Total Dissolved Solids — это общее количество растворенных веществ в напитке, формирующих вкус кофе.\n\n"
"• Измеряется в процентах (например, 1.30–1.50%)\n"
"• Экстракция — сколько веществ извлечено из зерна (идеал: 18–22%)\n\n"
"Факторы влияния:\n"
"• Размер помола\n"
"• Температура воды\n"
"• Время заваривания\n"
"• Качество воды\n\n"
"🎯 Совет: Недоэкстракция — вкус будет плоским,кислым. Переэкстракция — появится горечь."
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="info_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )

coffee_tds_handler = CallbackQueryHandler(show_coffee_tds, pattern="^info_tds$")
