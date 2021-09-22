from rest_framework.response import Response
from rest_framework import viewsets

from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from db.models import Event, Comment, Post
from db.api.serializer import CommentSerializer, PostSerializer, EventSerializer

class PostDetail(APIView):

        @classmethod
        def get_extra_actions(cls):
            return []

        def get_object(self, pk):
            try:
                return Post.objects.get(pk=pk)
            except Post.DoesNotExist:
                raise Http404

        def get(self, request, pk):
                post       = self.get_object(pk)
                serialized = PostSerializer(post)
                return Response(serialized.data)
        
        def delete(self, request, pk, format=None):
                post = self.get_object(pk)
                post.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

class CommentDetail(APIView):

        @classmethod
        def get_extra_actions(cls):
            return []

        def get_object(self, request, pk):
            try:
                return Comment.objects.get(pk=pk)
            except Comment.DoesNotExist:
                raise Http404

        def get(self, pk):
                comment      = self.get_object(pk)
                serialized   = CommentSerializer(comment)
                return Response(serialized.data)
        
        def delete(self, request, pk, format=None):
                comment = self.get_object(pk)
                comment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

class EventDetail(APIView):
        @classmethod
        def get_extra_actions(cls):
            return []

        def get_object(self, pk):
            try:
                return Event.objects.get(pk=pk)
            except Snippet.DoesNotExist:
                raise Http404

        def get(self, pk):
                print(pk)

                event      = self.get_object(pk)
                serialized = EventSerializer(event)
                return Response(serialized.data)
        
        def delete(self, request, pk, format=None):
                snippet = self.get_object(pk)
                snippet.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
                
class EventList(viewsets.ViewSet):

    @staticmethod
    def list(self):
        queryset        = Event.objects.all()
        serialized      = EventSerializer(queryset, many=True)

        return Response(serialized.data)

    @action(detail=True, methods=['get'])
    def user_events_list(self, user_id):
        #this contains all the event related with an specific user
        queryset		= Event.objects.get(user_owner=user_id)
        serialized		= EventSerializer(queryset, many=True)

        return Response(serialized.data)
		
    @action(detail=True, method=['get'])
    def date_list(self, date):
        #just contains all events in an specific date
        queryset		= Event.objects.get(date_created=date)
        serialized		= EventSerializer(queryset, many=True)

        return Response(serialized.data)
