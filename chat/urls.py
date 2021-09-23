from django.urls import path

from . import views

app_name = 'chatapp'

urlpatterns = [
	path('index/', views.index, name='index'),
	path('<str:room_name>/', views.room, name='room'),
	path('create_newchat/', views.create_new_chat, name='creator'),
	path('algo/', views.algo, name='algo')
]