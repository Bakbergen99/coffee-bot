from telegram import WebAppInfo  # <-- Тек осы жерден алынады!
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from telegram import Update
from telegram.ext import ContextTypes
from telegram.error import BadRequest

from handlers_subscription import handle_check_subscription
from check_subscription import is_user_subscribed
from handlers_subscription import handle_check_subscription

from handlers_battle import battle_rules, start_battle, handle_battle_answer
from handlers_solo import solo_rules, start_solo, handle_callback
from handlers_ranking import show_ranking
from utils import save_users, load_users
from handlers_menu import show_inline_main_menu as show_main_menu
from handlers_menu import show_inline_main_menu
from handlers_info_history import coffee_history_handler
from handlers_menu import info_menu_handler
from handlers_menu import main_menu_handler
from handlers_info import coffee_beans_handler
from handlers_info_grind import coffee_grind_handler
from handlers_info_tds import coffee_tds_handler
from handlers_info_v60 import v60_handler
from handlers_info_chemex import chemex_handler
from handlers_info_aeropress import aeropress_handler
from handlers_info_frenchpress import frenchpress_handler
from handlers_info_espresso import espresso_handler
from handlers_info_water import water_info_handler
from handlers_info_dose import dose_info_handler
from handlers_info_flavor import flavor_info_handler
from handlers_info_processing import processing_info_handler
from handlers_info_regions import regions_info_handler
from handlers_info_specialty import specialty_info_handler
from handlers_feedback import feedback_menu
from handlers_profile import user_profile
from handlers_battle import cancel_battle
from handlers_easter_egg import show_easter_egg
from handlers_superbaxa import superbaxa_rules, start_superbaxa, handle_superbaxa_answer
from handlers_about import show_about_bot
from handlers_menu_minigames import show_minigames_menu


users = load_users()

TOKEN = "7780315490:AAE3sa-iGiTo2e7Ogti8GvZXqt6f3b_0UK0"

async def test_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot = context.bot

    if await is_user_subscribed(bot, user_id):
        await update.message.reply_text("✅ Сіз тіркелгенсіз!")
    else:
        await update.message.reply_text("❌ Сіз тіркелмегенсіз!")

async def not_implemented(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.callback_query.message.edit_text(
            "🔧 Бұл бөлім жақында қосылады.\n\n🔙 Артқа үшін /start басыңыз"
        )
    except BadRequest as e:
        if "Message is not modified" in str(e):
            pass  # Ештеңе істеме
        else:
            raise  # Басқа қате шықса — көрсете сал

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Бас мәзірді шақыру
    app.add_handler(CommandHandler("start", show_main_menu))
    app.add_handler(CallbackQueryHandler(handle_check_subscription, pattern="check_subscription"))
    app.add_handler(CommandHandler("check", test_subscription))
    # Барлық CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(show_main_menu, pattern="^back_to_menu$"))  # Артқа
    app.add_handler(CallbackQueryHandler(show_main_menu, pattern="^start$"))         # /start командасынан
    app.add_handler(CallbackQueryHandler(solo_rules, pattern="^solo_rules$"))
    app.add_handler(CallbackQueryHandler(handle_callback, pattern="^(start_solo|restart_solo|back|back_to_menu)$"))
    app.add_handler(CallbackQueryHandler(show_ranking, pattern="^show_ranking$"))
    app.add_handler(info_menu_handler)         # Пайдалы ақпарат меню
    app.add_handler(coffee_history_handler)    # Кофе тарихы
    app.add_handler(main_menu_handler)
    app.add_handler(coffee_beans_handler)
    app.add_handler(coffee_grind_handler)
    app.add_handler(coffee_tds_handler)
    app.add_handler(v60_handler)
    app.add_handler(chemex_handler)
    app.add_handler(aeropress_handler)
    app.add_handler(frenchpress_handler)
    app.add_handler(espresso_handler)
    app.add_handler(water_info_handler)
    app.add_handler(dose_info_handler)
    app.add_handler(flavor_info_handler)
    app.add_handler(processing_info_handler)
    app.add_handler(regions_info_handler)
    app.add_handler(specialty_info_handler)
    app.add_handler(CallbackQueryHandler(feedback_menu, pattern="^feedback$"))
    app.add_handler(CallbackQueryHandler(user_profile, pattern="^profile$"))
    app.add_handler(CallbackQueryHandler(battle_rules, pattern="^battle_mode$"))
    app.add_handler(CallbackQueryHandler(start_battle, pattern="^start_battle$"))
    app.add_handler(CallbackQueryHandler(handle_battle_answer, pattern="^battle_ans_"))
    app.add_handler(CallbackQueryHandler(cancel_battle, pattern="^cancel_battle$"))
    app.add_handler(CallbackQueryHandler(show_easter_egg, pattern="^easter_eggs$"))
    app.add_handler(CallbackQueryHandler(superbaxa_rules, pattern="^superbaxa$"))
    app.add_handler(CallbackQueryHandler(start_superbaxa, pattern="^start_superbaxa$"))
    app.add_handler(CallbackQueryHandler(handle_superbaxa_answer, pattern="^sb_answer_"))
    app.add_handler(CallbackQueryHandler(show_about_bot, pattern="^about_bot$"))
    app.add_handler(CallbackQueryHandler(show_minigames_menu, pattern="^minigames_menu$"))

    # Уақытша бос режимдер (тек "жақында қосылады")
    app.add_handler(CallbackQueryHandler(not_implemented, pattern="^(latte_art|faq|suppliers)$"))

    # Соло режим логикасы
    app.add_handler(CallbackQueryHandler(handle_callback))

    print("🤖 Бот іске қосылды...")
    app.run_polling()

if __name__ == "__main__":
    main()

