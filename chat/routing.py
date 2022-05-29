from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/room/<room_name>/', consumers.ChatConsumer.as_asgi()),
]
