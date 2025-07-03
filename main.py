import requests
import random
import string
import schedule
import time
import os
from telegram import Bot

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
bot = Bot(token=TOKEN)

def generate_random_upi():
    prefix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 9)))
    suffix = random.choice(["@ybl", "@ibl", "@paytm", "@oksbi", "@okaxis"])
    return prefix + suffix

def check_campaign():
    upi = generate_random_upi()
    headers = {
        "Content-Type": "application/json",
        "appversion": "1.0",
        "appname": "loreal",
        "channel": "WEB"
    }

    payload = {
        "upi_id": upi
    }

    try:
        res = requests.post("https://web.myfidelity.in/api/loreal/check", json=payload, headers=headers, timeout=10)
        data = res.json()

        status = data.get("message", "No message")
        msg = f"📢 Campaign Response: {status}\n🔁 UPI Used: {upi}"
        bot.send_message(chat_id=CHAT_ID, text=msg)

    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"❌ Error: {str(e)}")

# Schedule to run every 1 hour
schedule.every(1).hours.do(check_campaign)

# First run instantly
check_campaign()

while True:
    schedule.run_pending()
    time.sleep(5)
