from .utils import send_telegram_message
from .message_enum import TelegramMessagesEnum


class TelegramHandlerWebHook:

    def __init__(self, chat_id, message):
        if chat_id and message:
            self.chat_id = chat_id
            self.message = message
        else:
            raise ValueError

    def run(self):
        self.__route_command()

    def __route_command(self):
        """
        Роутинг команд
        """
        if self.message.startswith("/start"):
            self.__start()
        else:
            send_telegram_message(self.chat_id, TelegramMessagesEnum.UNKNOWN_COMMAND.value)

    def __start(self):
        send_telegram_message(self.chat_id, TelegramMessagesEnum.GREETING.value,
                              web_app={"text": "VEEPN", "url": "https://veepn.nestforge.online"})
