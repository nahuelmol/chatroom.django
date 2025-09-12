from django.urls import path, include

from . import views

app_name = 'chatviews'

urlpatterns = [
	path('create/', 				views.create, name='create'),
	path('room/<str:name>/', 	    views.room, name='room'),
]
