from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = (
        'id', 'email', 'first_name', 'last_name', 'get_role_display',
        'tg_user_id', 'tg_username', 'created_at'
    )
    list_filter = ('role', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'first_name', 'last_name', 'tg_username', 'tg_user_id')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'role')
        }),
        ('Личная информация', {
            'fields': ('first_name', 'last_name', 'second_name', 'about')
        }),
        ('Telegram данные', {
            'fields': ('tg_user_id', 'tg_username', 'tg_first_name', 'tg_last_name')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'second_name', 'role',
                'tg_user_id', 'tg_username'
            ),
        }),
    )
