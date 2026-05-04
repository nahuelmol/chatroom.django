import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatroom.settings')

import django
django.setup()

import chat.routing

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

django_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.ws_urlpatterns
        )
    ),
})
