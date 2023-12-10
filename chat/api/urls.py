from rest_framework import routers
from django.urls import path
from chat.api.views import SaveChatroom, SaveFollower, SaveSubscriber

app_name = 'saver'
router = routers.SimpleRouter()

urlpatterns = [
	path('chatrooms/',		SaveChatroom.as_view(), name='chatrooms'),
	path('followers/',		SaveFollower.as_view(), name='followers'),
	path('subscribers/', 	SaveSubscriber.as_view(), name='subscribers'),
]

urlpatterns += router.urls