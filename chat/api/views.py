from rest_framework.views import APIView
from rest_framework import permissions, authentication

from django.shortcuts import redirect
from django.http import JsonResponse

from db.models import Chatroom, Follower

import datetime

class SaveFollower(APIView):

	authentication_classes = [
		authentication.TokenAuthentication]
	permission_classes = [
		permissions.AllowAny]

	def post(self, request):

		print(request.data)

		userid 		= request.data.get('id')
		username 	= request.data.get('username')

		new_follower	= Follower(
			followed_chatroom=chatroomid,
			followed_user=chatroom_creator_id,
			user_follower=userid,
			date_follow=date)

		try:
			new_follower.save()
			return JsonResponse({'mensaje': 'following successful'})
			
		except Exception as e:

			exe = str(e)

			if new_follower:
				return JsonResponse({'mensaje': 'following successful'})
			else:
				return JsonResponse({'mensaje': 'following successful'})


class SaveSubscriber(APIView):

	authentication_classes = [
		authentication.TokenAuthentication]
	permission_classes = [
		permissions.AllowAny]

	def post(self, request):

		print(request.data)

		userid 		= request.data.get('id')
		username 	= request.data.get('username')

		new_subscriber	= Subscriber(
			followed_user=chatroom_creator_id,
			user_subscriber=userid,
			date_follow=date)

		try:
			new_subscriber.save()
			return JsonResponse({'mensaje': 'Subscribed successfully'})
			
		except Exception as e:

			exe = str(e)

			if new_subscriber:
				return JsonResponse({'mensaje': 'Solicitud exitosa'})
			else:
				return JsonResponse({'mensaje': 'Solicitud exitosa'})



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
			return redirect('chatapp:index')
			
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

