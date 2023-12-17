from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from rest_framework import authentication

from django.http import HttpResponse

from django.contrib.auth.models import User
from db.models import Chatroom, Message
from db.views import create_chatroom

def explore(request):

	chat_list = Chatroom.objects.all()
	context = { 'chat_list': chat_list }

	if request.user.is_authenticated:
		username 	= request.user.username
		usr 		= User.objects.get(username=username)
		
		context = { 'chat_list': chat_list,
					'logged_user': usr }

	return render(request, 'explore.html', context)

def user_profile(request):

	userdata = User.objects.find(userid)

	context = {
		'chat_list': userdata,
	}

	return render(request, 'profile.html', context) 

def login(request):

	context = {
		'chat_list': 'login page',
	}

	return render(request, 'login.html', context)

@login_required(login_url='/admin/')
def feed(request):

	username 	= request.user.username
	usr 		= User.objects.get(username=username)

	chat_list = Chatroom.objects.all()
	
	context = {
		'chat_list': chat_list,
		'logged_user': usr
	}
	return render(request, 'feed.html', context) 

@login_required(login_url='/admin/')
def room(request, room_name):
	array 		= []
	msg_array 	= []
	currentuser = request.user.username
	is_owner 	= False

	for each in Chatroom.objects.all():
		array.append(each.chatroom_name)

	if not (room_name in array):
		return redirect('chatapp:feed')

	for each in Message.objects.all():
		if each.chatroom == 'chat_'+ room_name:
			msg_array.append(each)

	chatroom 	= Chatroom.objects.get(chatroom_name=room_name)
	author 		= chatroom.author

	if (currentuser == author):
		is_owner = True

	context = {	'room__name':room_name,
				'messages':msg_array,
				'is_owner':is_owner
		}

	return render(request, 'chatroom.html', context)