from django.urls import re_path
from . import consumers

ws_urlpatterns = [
	re_path(r'^ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
    re_path(r'^ws/notifications', consumers.NotificationConsumer.as_asgi())
]
