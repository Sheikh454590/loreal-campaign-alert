import os
import random
import time
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def random_upi():
    banks = ["@ybl", "@axl", "@paytm", "@ibl", "@okicici", "@oksbi"]
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(8, 11)))
    return name + random.choice(banks)

def check_campaign(upi):
    url = "https://web.myfidelity.in/api/upi-check"  # Example endpoint
    payload = {"upi": upi}
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("message", "No message")
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception: {str(e)}"

while True:
    upi = random_upi()
    result = check_campaign(upi)
    msg = f"🔁 Random UPI Checked: {upi}\n📢 Campaign Response: {result}"
    print(msg)
    bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")
    time.sleep(3600)  # Wait 1 hour
