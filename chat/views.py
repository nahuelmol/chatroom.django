from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse

from rest_framework import authentication
from itertools import chain

from db.models import Chatroom, Message, Follower, Subscriber
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

def profile(request):

	username 	= request.user.username
	user 		= User.objects.get(username=username)

	followers 	= Follower.objects.filter(followed_user=user) #user como seguido
	followeds 	= Follower.objects.filter(user_follower=user) #user como seguidor
	chats 		= Chatroom.objects.filter(author=username)

	users_followers = []
	users_followeds = []

	for follower in followers:
		ufwer = follower.user_follower
		users_followers.append(ufwer)

	for followed in followeds:
		ufwed = followed.followed_user
		users_followeds.append(ufwed)

	amountFollowers = followers.count()
	amountFolloweds = followeds.count()
	amountChatrooms = chats.count()

	fwers_list 	= followers.all()
	fweds_list 	= followeds.all()

	context  = {
		'userdata': user,
		'followers':amountFollowers,
		'followeds':amountFolloweds,
		'chatrooms':amountChatrooms,
		'fds_list':users_followeds,
		'frs_list':users_followers,
	}

	return render(request, 'profile.html', context) 

def register(request):
	user 	= request.user

	if user.is_authenticated:
		context = {
			'userdata': 'you need to be logged out',
		}

		return render(request, 'register.html', context)
	
	context = {
		'userdata': 'register page',
	}

	return render(request, 'register.html', context)

def login(request):


	username = request.user.username

	userdata = User.objects.get(username=username)

	context = {
		'userdata': userdata,
	}

	return render(request, 'login.html', context)


def logout(request):

	username = request.user.username

	userdata = User.objects.get(username=username)

	context = {
		'userdata': userdata,
	}

	return render(request, 'logout.html', context)

@login_required(login_url='/admin/')
def feed(request):

	username 	= request.user.username
	user 		= User.objects.get(username=username)

	follows 	= Follower.objects.filter(user_follower=user)
	
	chats_feed 	= []

	for each in follows:
		data = Chatroom.objects.filter(author=each.followed_user)

		if type(data) is list:
			chats_feed = chats_feed + data
		else:
			chats_feed.append(data)

	chats_ff = list(chain(*chats_feed))

	if not chats_ff:
		messages.info(request, "It seems that you don't have follow anyone!")

	context = {
		'chat_list': chats_ff,
		'logged_user': user
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