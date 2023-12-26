import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')
django.setup()  # Djangoを初期化

import chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # 通常のHTTPリクエスト
    "websocket": AuthMiddlewareStack(  # WebSocketリクエスト
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
