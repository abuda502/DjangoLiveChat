from django.urls import path
from . import consumers
#WebSocket connections using a single consumer class (ChatConsumer in this case) and route them to the appropriate chat room based on the room name passed as a parameter in the WebSocket URL.
websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),

 
]