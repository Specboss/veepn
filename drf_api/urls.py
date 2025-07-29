from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', include('drf_api.users.urls')),
    path('telegram/', include('drf_api.telegram.urls')),
    path('', include('drf_api.levels.urls')),
    path('', include('drf_api.posts.urls'))
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
