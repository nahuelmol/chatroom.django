from rest_framework.views import APIView
from rest_framework import permissions, authentication

from django.shortcuts import redirect

from db.models import Chatroom

import datetime

class SaveChatroom(APIView):

	authentication_classes = [
		authentication.TokenAuthentication]

	permission_classes = [
		permissions.AllowAny]
	
	def post(self, request):

		headers = request.META
		author 	= request.data.get('author')
		chatna 	= request.data.get('chatname')

		chats = []
		chats = Chatroom.objects.all()

		if chatna in chats:
			messages.add_message(request, messages.INFO, 'this chat name already exists, please choose other')
			return redirect('chatapp:index')

		result 			= datetime.datetime.now()
		time			= str(result.hour) +':'+str(result.minute)
		link 			= "http://localhost:8000"+"/"+chatna

		new_chat = Chatroom(
			chatroom_name=chatna,
			creation_date=time,
			author=author,
			link_to_join=link,
			)

		try:
			new_chat.save()
		except Exception as e:

			exe = str(e)

			if new_chat:
				messages.success(request, 'chatroom created: '+ exe)
				return redirect('chatapp:index')
			else:
				messages.success(request, 'chatroom not created: '+ exe)
				return redirect('chatapp:index')

	def get(self, request):

		messages.add_message(request, messages.INFO, 'get request arent allowed')
		return redirect('chatapp:index')

