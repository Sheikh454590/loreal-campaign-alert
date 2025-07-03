import requests

# 👉 Replace with your token & ID
BOT_TOKEN = "8151085825:AAE42arT42Tu0TvFX5jHmf01Xa29rUrApRI"
USER_ID = "6314543436"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": USER_ID,
        "text": msg
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram send failed:", e)

def check_campaign():
    url = "https://web.myfidelity.in/loreal/api/redemption/getStatus"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        message = f"📢 Campaign Response:\n\n📝 Status: {data.get('msg')}\n📦 Code: {data.get('code')}"
        send_telegram(message)
        print("✅ Telegram sent:", message)
    except Exception as e:
        send_telegram(f"⚠ Error checking campaign: {e}")
        print("❌ Error:", e)

if __name__ == "__main__":
    check_campaign()
