import os
from rest_framework import serializers

from .auth_telegram import verify_telegram_init_data


class TelegramAuthSerializer(serializers.Serializer):
    initData = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=["author", "user"], required=False, default="user")

    def validate_initData(self, value):
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        try:
            data = verify_telegram_init_data(value, bot_token)
        except ValueError as e:
            raise serializers.ValidationError(str(e))
        return data
