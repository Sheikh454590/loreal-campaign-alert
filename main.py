import os
import requests
from telegram import Bot

# ✅ Step 1: Fetch token and chat_id from environment
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# ✅ Step 2: Validate environment variables
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found in environment variables.")
if not CHAT_ID:
    raise ValueError("❌ CHAT_ID not found in environment variables.")

# ✅ Step 3: Initialize bot
bot = Bot(token=BOT_TOKEN)

# ✅ Step 4: Sample Redemption check request
def check_campaign():
    try:
        res = requests.post(
            "https://web.myfidelity.in/api/v1/loreal_standup/redemption",
            json={"redemptionType": "CASHBACK"},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        return res.text
    except Exception as e:
        return f"❌ Error: {e}"

# ✅ Step 5: Send result to Telegram
status = check_campaign()
bot.send_message(chat_id=CHAT_ID, text=f"🧾 Redemption Status:\n{status}")
