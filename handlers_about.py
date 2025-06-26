from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ContextTypes

async def show_about_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
            "📖 Бот туралы / О боте\n\n"
            "🤎 Бұл бот – кофе мәдениетіне деген шексіз махаббатпен және адал еңбекпен жасалған жоба.\n"
            "🧑‍💻 Оны кәсіби программист емес, бариста мамандығын игерген адам жалғыз өзі жасап шықты.\n"
            "🧩 Ішінде кейбір қателіктер, техникалық ақаулар кездесуі мүмкін. Сол үшін түсіністікпен қарауыңызды сұраймын.\n"
            "🚀 Бұл бот күн сайын дамып, жаңарып отырады – алда әлі көп қызықтар!\n"
            "🌙 Ұйқысыз түндер, сынақтар мен шабытты сәттер нәтижесінде сіздің алдыңызда осы бот пайда болды.\n\n"
            "🤎 Этот бот создан с огромной любовью к кофейной культуре и преданностью делу.\n"
            "🧑‍💻 Его разработал не профессиональный программист, а бариста — полностью в одиночку.\n"
            "🧩 Внутри возможны небольшие ошибки или баги, прошу отнестись с пониманием.\n"
            "🚀 Бот развивается и обновляется каждый день — впереди ещё много интересного!\n"
            "🌙 Бессонные ночи, тесты и вдохновение — всё ради вас и вашего интереса.\n\n"
            "☕ Powered by passion. Crafted by SuperBaxa"
    )

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]
    ]

    await update.callback_query.message.edit_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
