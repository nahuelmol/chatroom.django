from django.urls import path

from . import views

app_name = 'chatapp'

urlpatterns = [
	path('explore/' , 			views.explore, name='explore'),
	path('profile/', 			views.user_profile, name='profile'),
	path('login/', 				views.login, name='login'),
	path('feed/', 				views.feed, name='feed'),
	path('<str:room_name>/', 	views.room, name='room'),
]