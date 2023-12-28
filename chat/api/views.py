from rest_framework.views import APIView
from rest_framework import permissions, authentication

from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from db.models import Chatroom, Follower, Subscriber
from db.forms import RegistrationForm

import datetime

class user_register(APIView):

	def post(self, request):
		form = RegistrationForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(resquest, user)

			return redirect('chatapp:feed')
		else:
			return redirect('chatapp:register')
	

		context = {
			'userdata': 'login page',
		}

		return render(request, 'register.html', context)

class user_login(APIView):

	def post(self, resquest):

		username = request.data.get('username')
		password = request.data.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('chatapp:feed')
		else:
			return redirect('chatapp:login')
	
def findroom(roomname):

	try:
		chatroom = Chatroom.objects.get(chatroom_name=roomname)
		return chatroom

	except Chatroom.DoesNotExist:
		return None


def findowner(owner):

	try:
		user = User.objects.get(username=owner)
		return user
	except User.DoesNotExist:
		return None



class SaveFollower(APIView):

	authentication_classes = [
		authentication.TokenAuthentication]
	permission_classes = [
		permissions.AllowAny]

	def post(self, request, room_name):

		userid 		= request.data.get('id')
		username 	= request.data.get('username')

		chatroom 	= findroom(room_name)
		owner 		= findowner(chatroom.author)

		follower = User.objects.get(username=username)

		today 			= datetime.datetime.now()
		
		new_follower	= Follower(
			followed_user=owner,
			user_follower=follower,
			date_follow=today)

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

	def post(self, request, room_name):

		userid 		= request.data.get('id')
		username 	= request.data.get('username')

		chatroom 	= findroom(room_name)
		owner 		= findowner(chatroom.author)

		subscriber 	= User.objects.get(username=username)

		today 			= datetime.datetime.now()

		new_subscriber	= Subscriber(
			subscribed_user=owner,
			follower_subscriber=subscriber,
			date_subs=today)

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
		chat 	= request.POST.get('chatname')
		user 	= request.POST.get('username')

		print(user)

		chats = []
		chats = Chatroom.objects.all()

		if chat in chats:
			messages.add_message(request, messages.INFO, 'this chat name already exists, please choose other')
			return redirect('chatapp:explore')

		result 			= datetime.datetime.now()
		time			= str(result.hour) +':'+str(result.minute)
		link 			= "http://localhost:8000/chat/room/"+chat

		new_chat = Chatroom(
			chatroom_name=chat,
			creation_date=time,
			author=user,
			link_to_join=link,
			)

		try:
			new_chat.save()
			return redirect('chatapp:explore')
			
		except Exception as e:

			exe = str(e)

			if new_chat:
				messages.success(request, 'chatroom created: '+ exe)
				return redirect('chatapp:explore')
			else:
				messages.success(request, 'chatroom not created: '+ exe)
				return redirect('chatapp:explore')

	def get(self, request):

		messages.add_message(request, messages.INFO, 'get request arent allowed')
		return redirect('chatapp:explore')

