from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from telegram.ext import CallbackQueryHandler
from check_subscription import is_user_subscribed


async def show_inline_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    if not await is_user_subscribed(bot, user_id):
        await update.effective_chat.send_message(
            text="📢 Ботты қолдану үшін алдымен біздің арнаға тіркеліңіз: @barista_club_kz\n"
                "✅ Тіркелген соң төмендегі 'Қайта тексеру' батырмасын басыңыз.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 Қайта тексеру", callback_data="check_subscription")]
            ])
        )
        return


    keyboard = [
        [InlineKeyboardButton("👤 Соло режим", callback_data="solo_rules")],
        [InlineKeyboardButton("⚔️ 1x1 Баттл", callback_data="battle_mode")],
        [InlineKeyboardButton("😈 SuperBaxa режим", callback_data="superbaxa")],
        [InlineKeyboardButton("☕ Латте-арт", callback_data="latte_art")],
        [InlineKeyboardButton("🎮 Мини ойындар", callback_data="minigames_menu")],
        [InlineKeyboardButton("📜 Пайдалы акпарат", callback_data="info_menu")],
        [InlineKeyboardButton("🏆 Рейтинг", callback_data="show_ranking")],
        [InlineKeyboardButton("🧩 Пасхалка", callback_data="easter_eggs")],
        [InlineKeyboardButton("💬 Кері байланыс/ Фидбек", callback_data="feedback")],
        [InlineKeyboardButton("👤 Мен туралы / Обо мне", callback_data="profile")],
        [InlineKeyboardButton("📖 Бот туралы / О боте", callback_data="about_bot")],

        [InlineKeyboardButton("📍 Поставщики / Жеткізушілер", callback_data="suppliers")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        await update.callback_query.message.delete()
    except:
        pass

    await update.effective_chat.send_message(
        "🏠 *Басты мәзір* / Главное меню",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


async def show_info_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()

    keyboard = [
    [InlineKeyboardButton("☕ Кофенің тарихы / История кофе", callback_data="info_history")],
    [InlineKeyboardButton("🌱 Кофе дәндері / Кофейные зерна", callback_data="info_beans")],
    [InlineKeyboardButton("⚙️ Дұрыс ұнтақтау / Настройка помола", callback_data="info_grind")],
    [InlineKeyboardButton("📐 TDS, экстракция", callback_data="info_tds")],
    [InlineKeyboardButton("🫖 V60", callback_data="info_v60")],
    [InlineKeyboardButton("🧪 Chemex", callback_data="info_chemex")],
    [InlineKeyboardButton("🚀 Aeropress", callback_data="info_aeropress")],
    [InlineKeyboardButton("🫙 French Press", callback_data="info_frenchpress")],
    [InlineKeyboardButton("⚡ Эспрессо әдісі", callback_data="info_espresso")],
    [InlineKeyboardButton("🌡️ Су температурасы / Температура воды", callback_data="info_water")], 
    [InlineKeyboardButton("🎛️ Дозировка және рецепт / Дозировка и рецепт", callback_data="info_dose")],
    [InlineKeyboardButton("📊 Дәм профилі / Вкусовой профиль", callback_data="info_flavor")],
    [InlineKeyboardButton("🧼 өңдеу тәсілдері / Способы обработки", callback_data="info_processing")],
    [InlineKeyboardButton("🌍 Аймақтар дәмі / Страны и регионы", callback_data="info_regions")],
    [InlineKeyboardButton("🌟 Specialty кофе", callback_data="info_specialty")],

    [InlineKeyboardButton("🔙 Артқа / Назад", callback_data="main_menu")]
]



    await update.callback_query.edit_message_text(
        text="📚 <b>Пайдалы ақпарат / Полезная информация</b>\n\nБөлімді таңдаңыз:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="HTML"
    )
    

info_menu_handler = CallbackQueryHandler(show_info_menu, pattern="^info_menu$")
main_menu_handler = CallbackQueryHandler(show_inline_main_menu, pattern="^main_menu$")