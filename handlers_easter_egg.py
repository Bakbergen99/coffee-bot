from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import random

# Екі тілде пасхалка фразалары
EASTER_EGGS = [
    "😈 SuperBaxa былай дейді:\n\"Мен бәрін бақылап жүрмін... Тағы 1 қателік – және сен менімен бетпе-бет қаласың.\"\n\n😈 SuperBaxa говорит:\n\"Я наблюдаю за тобой... Ещё одна ошибка — и ты встретишься со мной.\"",

    "☕ Факт:\nБір шыны кофе жасау үшін шамамен 140 литр су қажет (өсірілуінен бастап дайындалуына дейін).\n\n☕ Факт:\nНа один стакан кофе уходит около 140 литров воды — от выращивания до чашки.",

    "🧠 Қызық:\nЭспрессо деген сөз итальянша 'қысыммен дайындалған' деген мағынаны білдіреді!\n\n🧠 Интересно:\nСлово 'Эспрессо' означает 'приготовленный под давлением' на итальянском.",

    "🎭 Мем:\n\"Кофе – менің психологиялық Wi-Fi-ым\".\n\n🎭 Мем:\n\"Кофе — это мой психологический Wi-Fi\".",

    "🕵️‍♂️ Құпия код:\nПасхалка коды: <code>superbaxa2025</code> – дұрыс жерге енгізсең, бонус күтіп тұр.\n\n🕵️‍♂️ Секретный код:\nКод пасхалки: <code>superbaxa2025</code> — если введешь в нужном месте, получишь бонус."
]

async def show_easter_egg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    message = random.choice(EASTER_EGGS)

    keyboard = [
        [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]
    ]

    await update.callback_query.edit_message_text(
        text=f"🧩 <b>Пасхалка / Easter Egg</b>\n\n{message}",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )
