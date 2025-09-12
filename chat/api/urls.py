from rest_framework import routers
from django.urls import path
from chat.api.views import SaveChatroom, SaveFollower, SaveSubscriber

app_name = 'chatapi'
router = routers.SimpleRouter()

urlpatterns = [
	path('create/',						SaveChatroom.as_view(), name='save'),
	path('follow/<str:name>/',			SaveFollower.as_view(), name='followers'),
	path('subscribe/<str:name>', 		SaveSubscriber.as_view(), name='subscribers'),
]

urlpatterns += router.urls
