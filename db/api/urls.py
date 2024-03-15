from rest_framework import routers
from django.urls import include, path

from db.api.views import EventList, PostDetail, CommentDetail, EventDetail

app_name = 'db-app'
router = routers.SimpleRouter() 

unique_event	= EventDetail
#all_events		= EventList.as_view({'get':'list'})
#date_events		= EventList.as_view({'get':'date_list'})
#user_events		= EventList.as_view({'get':'user_events_list'})

#router.register(r'event/<int:pk>', 		unique_event,	basename='event')	
#router.register(r'events/:<date>',		date_events,	basename='events-in')
#router.register(r'events/:<user_id>', 	user_events,	basename='user-events')
#router.register(r'events/', 			all_events,		basename='all-events')

urlpatterns = [
	path('event/<int:pk>', EventDetail.as_view()),
	path('api/', include(router.urls))
]
