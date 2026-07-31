from rest_framework import routers
from django.urls import path
from chat.api.views import SaveChatroom, SaveFollower, SaveSuscriptor

app_name = 'chatapi'
router = routers.SimpleRouter()

urlpatterns = [
	path('create/',						SaveChatroom.as_view(), name='save'),
	path('follow/<str:name>/',			SaveFollower.as_view(), name='followers'),
	path('subscribe/<str:name>/', 		SaveSuscriptor.as_view(), name='subs'),
]

urlpatterns += router.urls
