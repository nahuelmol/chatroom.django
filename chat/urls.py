from django.urls import path

from . import views

app_name = 'chatapp'

urlpatterns = [
	path('explore/' , 				views.explore, name='explore'),
	path('profile/', 				views.profile, name='profile'),
	path('login/', 					views.login, name='login'),
	path('register/',				views.register, name='register'),
	path('logout/', 				views.logout, name='logout'),
	path('feed/', 					views.feed, name='feed'),
	path('room/<str:room_name>/', 	views.room, name='room'),
]