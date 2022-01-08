from rest_framework.views import APIView
from rest_framework import permissions

from django.shortcuts import redirect

from db.models import Chatroom

import datetime

class SaveChatroom(APIView):

	permission_classes = [
		permissions.AllowAny]
	
	def post(self, request):

		author 	= request.data.get('author')
		chatna 	= request.data.get('chatname')

		result 			= datetime.datetime.now()
		time			= str(result.hour) +':'+str(result.minute)
		link 			= "http://localhost:8000"+"/"+chatna

		new_chat = Chatroom(
			chatroom_name=chatna,
			creation_date=time,
			author=author,
			link_to_join=link,
			)

		new_chat.save()

		return redirect('chatapp:index')



