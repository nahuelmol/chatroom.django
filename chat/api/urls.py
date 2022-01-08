from rest_framework import routers
from django.urls import path
from chat.api.views import SaveChatroom

app_name = 'saver'
router = routers.SimpleRouter()

urlpatterns = [
	path('chatrooms/',		SaveChatroom.as_view(), name='chatrooms'),
]

urlpatterns += router.urls