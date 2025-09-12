from django.urls import path, include

from . import views

app_name = 'chatviews'

urlpatterns = [
	path('create/', 				views.create, name='create'),
	path('/', 				        views.about, name='about'),
	path('room/<str:name>/', 	    views.room, name='room'),
]
