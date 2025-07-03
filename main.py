import os
import time
import random
import requests
from telegram import Bot
from telegram.constants import ParseMode

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def generate_upi():
    banks = ["@ybl", "@ibl", "@okaxis", "@paytm", "@upi", "@oksbi"]
    prefix = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=random.randint(6, 10)))
    return prefix + random.choice(banks)

def check_campaign(upi_id):
    try:
        url = "https://web.myfidelity.in/loreal/loreal-campaign/api/redeem"
        payload = {
            "upi": upi_id,
            "redeem_option": "cashback",
            "referral_code": ""
        }
        headers = {
            "Content-Type": "application/json",
            "appversion": "1.0",
            "appname": "loreal",
            "channel": "WEB"
        }
        res = requests.post(url, json=payload, headers=headers)
        data = res.json()
        message = data.get("message", "No message")
        print(f"[{upi_id}] ➜ {message}")
        return message
    except Exception as e:
        return f"Error: {e}"

def send_to_telegram(msg):
    try:
        bot.send_message(chat_id=CHAT_ID, text=f"📢 Campaign Check Result\n\n{msg}", parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Telegram Error: {e}")

while True:
    upi = generate_upi()
    result = check_campaign(upi)
    send_to_telegram(f"🔎 UPI Checked: {upi}\n🧾 Server Says: {result}")
    time.sleep(3600)  # every 1 hour
