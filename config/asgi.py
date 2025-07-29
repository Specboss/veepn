import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from drf_api.posts.middleware import TokenAuthMiddlewareStack
from drf_api.posts.routing import posts_websokcet_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddlewareStack(
        URLRouter(
            posts_websokcet_urlpatterns
        )
    ),
})
