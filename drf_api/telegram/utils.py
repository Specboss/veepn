import requests
import os


def send_telegram_message(chat_id, text, button=None, web_app=None):
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    if button or web_app:
        inline_keyboard = []
        if button:
            inline_keyboard.append([{
                "text": button["text"],
                "url": button["url"]
            }])
        if web_app:
            inline_keyboard.append([{
                "text": web_app["text"],
                "web_app": {
                    "url": web_app["url"]
                }
            }])
        payload["reply_markup"] = {
            "inline_keyboard": inline_keyboard
        }
    requests.post(url, json=payload)
