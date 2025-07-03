import os
import requests
import json
import random
from telegram import Bot
import time

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found in environment variables.")

if not CHAT_ID:
    raise ValueError("❌ CHAT_ID not found in environment variables.")

bot = Bot(token=BOT_TOKEN)

def generate_random_upi():
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
    domain = random.choice(['ybl', 'ibl', 'axl', 'upi', 'okaxis', 'okicici', 'oksbi'])
    return f"{name}@{domain}"

def check_campaign_status():
    msisdn = "9" + ''.join(random.choices("0123456789", k=9))
    headers = {
        "msisdn": msisdn,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "channel": "WEB",
        "channelname": "abc",
        "appversion": "1.0",
        "appname": "loreal",
        "campaignid": "100778999",
        "clientid": "d19LVB6rGlj6HAfR3h7CmZeEusVQedJAXd+Op30uqC4=",
        "devicetype": "a",
        "applanguage": "en",
        "User-Agent": "Mozilla/5.0 (Linux; Android 15)",
        "Origin": "https://microsite.ad.paytm.com",
        "Referer": "https://microsite.ad.paytm.com/",
        "X-Requested-With": "mark.via.gp"
    }

    payload = {"redemptionType": "CASHBACK"}
    try:
        response = requests.post(
            "https://web.myfidelity.in/api/v1/loreal_standup/redemption",
            headers=headers,
            json=payload,
            timeout=10
        )
        res_json = response.json()
        msg = res_json.get("msg", "❌ Unknown Response")
        code = res_json.get("code", "???")
        print(f"🔁 Response: {msg} | Code: {code}")

        # Send every message every time
        bot.send_message(chat_id=CHAT_ID, text=f"ℹ Campaign Check:\nUPI: {generate_random_upi()}\nStatus: {msg}")

        # If campaign active (i.e. not closed), alert
        if "Redemption window is closed" not in msg:
            bot.send_message(chat_id=CHAT_ID, text=f"✅ ALERT: Campaign seems ACTIVE!\nResponse: {msg}")
    except Exception as e:
        print(f"❌ Error: {e}")
        bot.send_message(chat_id=CHAT_ID, text=f"❌ ERROR in Campaign Checker:\n{str(e)}")

# 🔁 You can schedule this every 1 hour via CRON (Render or elsewhere)
check_campaign_status()
