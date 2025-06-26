import json, httpx
from telegram import Update
from telegram.ext import ContextTypes

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    user_id = update.effective_user.id
    print(f"📨 Хабарлама: {message}\n👤 ID: {user_id}")

    await update.message.reply_text("⏳ Жауап дайындалып жатыр...")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://t.me/testdixan_bot",  # нақты Telegram ботыңның username
        "X-Title": "Bakber AI Bot"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
            result = response.json()
            if "choices" in result:
                answer = result["choices"][0]["message"]["content"]
            else:
                answer = f"⚠️ Қате: {result}"
    except Exception as e:
        answer = f"🔥 Қате болды: {str(e)}"

    await update.message.reply_text(answer)
