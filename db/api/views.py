from rest_framework.response import Response
from rest_framework import viewsets

from db.models import Event
from db.api.serializer import CommentSerializer, PostSerializer, EventSerializer

class EventDetail(APIView):

        def get_object(self, pk):
            try:
                return Event.objects.get(pk=pk)
            except Snippet.DoesNotExist:
                raise Http404

        def get(self, pk=pk):
                event      = self.get_object(pk)
                serialized = EventSerializer(event)
                return Response serialized.data
        
        def delete(self, request, pk, format=None):
                snippet = self.get_object(pk)
                snippet.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
                

class EventsList(viewsets.ViewSet):

	@action(detail=True, methods=['get'])
    @staticmethod
    def list(self):
        queryset        = Event.objects.all()
        serialized      = EventSerializer(queryset, many=True)

        return Response(serialized.data)

    @action(detail=True, methods=['get'])
	def user_events_list(self, user_id):
		#this contains all the event related with an specific user
		queryset		= Event.objects.all(foreign_key=user_id)
		serialized		= EventSerializer[queryset, many=True]

		return Response(serialized.data)

	def date_list(self, date):
		#just contains all events in an specific date
		queryset		= Event.objects.all()
		serialized		= EventSerializer[queryset, many=True]

		return Response(serialized.data)
