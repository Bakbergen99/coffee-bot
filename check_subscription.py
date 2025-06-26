from telegram.error import BadRequest

async def is_user_subscribed(bot, user_id):
    try:
        chat_id = -1002762687773  # нақты ID
        print(f"[DEBUG] Checking subscription for user {user_id} in {chat_id}")
        member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
        return member.status in ["member", "administrator", "creator"]
    except BadRequest as e:
        print(f"⛔ [ERROR] Telegram API Error: {e}")
        return False