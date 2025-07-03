import requests

TOKEN = "8151085825:AAE42arT42Tu0TvFX5jHmf01Xa29rUrApRI"
CHAT_ID = "6314543436"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass

def check_campaign():
    headers = {
       "Content-Type":"application/json",
       "Accept":"application/json",
       "msisdn":"9999999999",
       "appversion":"1.0",
       "appname":"loreal",
       "channel":"WEB",
       "campaignid":"100778999",
       "clientid":"d19LVB6rGlj6HAfR3h7CmZeEusVQedJAXd+Op30uqC4="
    }
    res = requests.post(
        "https://web.myfidelity.in/api/v1/loreal_standup/redemption",
        json={"redemptionType": "CASHBACK"},
        headers=headers,
        timeout=10
    )
    if "Redemption window is closed" not in res.text:
        send_telegram("🎉 Campaign is ACTIVE! Run your full script NOW!")
    else:
        print("⏳ Still closed...")

if _name_ == "_main_":
    check_campaign()
