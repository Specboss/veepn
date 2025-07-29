from django.urls import path
from .views import UsersApiView

urlpatterns = [
    path('profile/', UsersApiView.as_view(), name='user-api'),
]
