from rest_framework.response import Response
from rest_framework import viewsets

from db.models import Event
from db.api.serializer import CommentSerializer, PostSerializer, EventSerializer

class EventsView(viewsets.ViewSet):

	@action(detail=True, methods=['get'])
	@staticmethod
	def retrieve(self, event_id):
		queryset		= Event.objects.all(pk=event_id)
		serialized		= EventSerializer(queryset, many=True)

		return Response(serialized.data)

	@action(detail=True, methods=['get'])
    @staticmethod
    def list(self):
        queryset        = Cat.objects.all()
        serialized      = CatSerializer(queryset, many=True)

        return Response(serialized.data)

    @action(detail=True, methods=['get'])
	def user_events_list(self, user_id):
		#this contains all the event related with an specific user
		queryset		= Event.objects.get(foreign_key=user_id)
		serialized		= EventSerializer[queryset, many=True]

		return Response(serialized.data)

	def date_list(self, date):
		#just contains all events in an specific date
		queryset		= Event.objects.get(date_created=date)
		serialized		= EventSerializer[queryset, many=True]

		return Response(serialized.data)