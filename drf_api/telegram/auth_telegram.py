import hashlib
import hmac
import json
import logging

from urllib.parse import unquote
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string

from app.users.models import User

logger = logging.getLogger(__name__)


def verify_telegram_init_data(init_data: str, bot_token: str) -> dict:
    vals = {}
    for pair in init_data.split('&'):
        k, v = pair.split('=', 1)
        vals[k] = unquote(v)
    received_hash = vals.pop('hash', None)
    if not received_hash:
        raise ValueError("Missing 'hash' parameter in init_data")
    data_check_string = '\n'.join(f"{k}={vals[k]}" for k in sorted(vals.keys()))
    if 'user' in vals:
        vals['user'] = json.loads(vals['user'])
    secret_key = hmac.new(b"WebAppData", bot_token.encode(), hashlib.sha256).digest()
    calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
    if calculated_hash != received_hash:
        raise ValueError("Invalid initData hash")
    return vals


class TelegramAuth:
    def __init__(self, init_data, role):
        user_data = init_data["user"]
        self.telegram_id = int(user_data["id"])
        self.username = user_data.get("username", "")
        self.first_name = user_data.get("first_name", "")
        self.last_name = user_data.get("last_name", "")
        self.role = role
        self.avatar = user_data.get('photo_url', None)
        self.user = None
        self.created = None

    def __update_avatar(self):
        if self.avatar and self.user.avatar != self.avatar:
            self.user.avatar = self.avatar
            self.user.save(update_fields=["avatar"])

    def execute(self):
        self.user, self.created = User.objects.get_or_create(
            tg_user_id=self.telegram_id,
            defaults={
                "email": f"{self.telegram_id}@telegram.local",
                "username": f"tg_{self.telegram_id}",
                "first_name": self.first_name,
                "last_name": self.last_name,
                "tg_username": self.username,
                "tg_first_name": self.first_name,
                "tg_last_name": self.last_name,
                "avatar": self.avatar,
                "role": self.role,
                "password": make_password(get_random_string(12))
            }
        )
        if not self.created:
            self.__update_avatar()

    def get_token(self) -> RefreshToken:
        return RefreshToken.for_user(self.user)
