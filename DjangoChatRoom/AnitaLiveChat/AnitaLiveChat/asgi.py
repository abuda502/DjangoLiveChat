import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing
from room.consumers import ChatConsumer
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AnitaLiveChat.settings')
django_asgi_app = get_asgi_application()

ASGI_APPLICATION = "AnitaliveChat.asgi.application"

# Add this block
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns)
        )
    ),
})
