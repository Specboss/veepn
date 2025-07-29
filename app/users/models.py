from django.contrib.auth.models import AbstractUser
from django.core.files.storage import storages
from django.db import models


def upload_to_avatars(instance, filename):
    return f"users/avatars/user_{instance.id}/{filename}"


class User(AbstractUser):
    """
    Пользователь
    """
    ROLE_CHOICES = [
        ('author', 'Автор'),
        ('user', 'Пользователь'),
    ]

    first_name = models.CharField("Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField("Фамилия", max_length=50, blank=True, null=True)
    second_name = models.CharField("Отчество", max_length=50, blank=True, null=True)
    email = models.EmailField('E-mail адрес', unique=True)
    avatar = models.ImageField(upload_to=upload_to_avatars,
                               null=True,
                               blank=True,
                               verbose_name='Аватар',
                               storage=storages["minio"])
    updated_at = models.DateTimeField("Дата последнего обновления", auto_now=True)
    created_at = models.DateTimeField("Дата регистрации", auto_now_add=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text="Группы, к которым принадлежит этот пользователь.",
        verbose_name="Группы"
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text="Конкретные разрешения для этого пользователя.",
        verbose_name="Права пользователя"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
