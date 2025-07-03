import requests
import random
import string
import json
import telegram

# Telegram setup
BOT_TOKEN = '8151085825:AAE42arT42Tu0TvFX5jHmf01Xa29rUrApRI'
USER_ID = '6314543436'
bot = telegram.Bot(token=BOT_TOKEN)

# Create random UPI
def random_upi():
    prefix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 10)))
    suffixes = ['@ibl', '@ybl', '@axl', '@paytm', '@upi', '@oksbi', '@okaxis']
    return prefix + random.choice(suffixes)

# Main function
def check_campaign():
    upi = random_upi()
    url = "https://web.myfidelity.in/api/v1/user/save-upi"
    headers = {
        "Content-Type": "application/json",
        "appversion": "1.0",
        "appname": "loreal",
        "channel": "WEB"
    }
    payload = {
        "vpa": upi
    }

    try:
        res = requests.post(url, headers=headers, json=payload, timeout=10)
        data = res.json()
    except Exception as e:
        bot.send_message(chat_id=USER_ID, text=f"❌ Error while calling API:\n{str(e)}")
        return

    msg = f"🕒 Checked UPI: {upi}\n📢 Campaign Response:\njson\n{json.dumps(data, indent=2)}"
    bot.send_message(chat_id=USER_ID, text=msg, parse_mode="Markdown")

# Run the check
check_campaign()
