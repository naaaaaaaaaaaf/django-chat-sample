from chat.consumers import ChatConsumer

from django.urls import path

websocket_urlpatterns = [
    path('ws/room/<str:room_id>', ChatConsumer.as_asgi()),
]
