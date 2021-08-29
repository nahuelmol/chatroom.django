from rest_framework.response import Response
from rest_framework import viewsets

from db.models import Event
from db.api.serializer import CommentSerializer, PostSerializer, EventSerializer

class EventsView(viewsets.ViewSet):

	@action(detail=True, methods=['get'])
	@staticmethod
	def retrieve(self):
		queryset		= Event.objects.all()
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
		queryset		= Event.objects.all()
		serialized		= EventSerializer[queryset, many=True]

		return Response(serialized.data)

	def mylist():
		queryset		= Event.objects.all()
		serialized		= EventSerializer[queryset, many=True]

		return Response(serialized.data)