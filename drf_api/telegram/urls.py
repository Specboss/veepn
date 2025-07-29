from django.urls import path
from . import views

urlpatterns = [
    path('webhook/', views.telegram_webhook, name='telegram-webhook-api'),
    path('auth/', views.TelegramAuthApiView.as_view(), name='telegram-auth-api'),
]
