from rest_framework import serializers

from app.levels.models import LevelUser
from app.posts.models import Post
from app.users.models import User


class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField(read_only=True)
    subscribers = serializers.SerializerMethodField(read_only=True)
    posts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "second_name", "email",
            "tg_user_id", "tg_username", "tg_first_name", "tg_last_name",
            "role", "role_name", "subscribers", "posts"
        ]
        read_only_fields = ["id", "tg_user_id", "tg_username", "tg_first_name", "tg_last_name"]

    def get_role_name(self, user):
        return user.get_role_display()

    def get_subscribers(self, user):
        return LevelUser.objects.filter(level__author=user).count()

    def get_posts(self, user):
        return Post.objects.filter(level__author=user).count()
