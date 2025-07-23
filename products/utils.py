import os
import requests
from dotenv import load_dotenv
load_dotenv()

def notify_telegram(user):
    if user.telegram_id:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not token:
            print("Токен не найден")
            return

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": user.telegram_id,
            "text": "Вам пришёл новый заказ!"
        }

        response = requests.post(url, data=data)
