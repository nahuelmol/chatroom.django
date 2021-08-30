from rest_framework import routers

from db.api.views import EventsView

app_name = '_api_'
router = routers.DefaultRouter() 

unique_event	= EventsDetail.as_view()
all_events		= EventsView.as_view({'get':'list'})
date_events		= EventsView.as_view({'get':'date_list'})
user_events		= EventsView.as_view({'get':'user_events_list'})

router.register(r'events/:<pk>', 		unique_event,	basename='event')	
router.register(r'events/:<date>',		date_events,	basename='events-in')
router.register(r'events/:<user_id>', 	user_events,	basename='user-events')
router.register(r'events/', 			all_events,		basename='all-events')

urlpatterns = router.urls
