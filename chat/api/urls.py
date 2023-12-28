from rest_framework import routers
from django.urls import path
from chat.api.views import SaveChatroom, SaveFollower, SaveSubscriber
from chat.api.views import user_register, user_login

app_name = 'saver'
router = routers.SimpleRouter()

urlpatterns = [
	path('chatrooms/',						SaveChatroom.as_view(), name='chatrooms'),
	path('follow/<str:room_name>/',			SaveFollower.as_view(), name='followers'),
	path('subscribe/<str:room_name>', 		SaveSubscriber.as_view(), name='subscribers'),
	path('user_register/',					user_register.as_view(), name='user_register'),
	path('user_login/', 					user_login.as_view(), name='user_login'),
]

urlpatterns += router.urls