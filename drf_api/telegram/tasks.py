from typing import NewType

from celery import shared_task
from .telegram_handler import TelegramHandlerWebHook
from .utils import send_telegram_message

FileName = NewType('FileName', str)
Content = NewType('Content', bytes)
MIME_Type = NewType('MIME_Type', str)


@shared_task
def telegram_webhook_task(chat_id, message):
    tg = TelegramHandlerWebHook(chat_id, message)
    tg.run()


@shared_task
def send_telegram_message_task(chat_id, text, button=None):
    send_telegram_message(chat_id, text, button)
