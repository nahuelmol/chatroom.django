from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django import forms

from rest_framework import authentication
from itertools import chain

from db.models import Chatroom, Message, Follower, Subscriber

def register(request):
	user 	= request.user
	if user.is_authenticated:
		context = {
			'userdata': 'you have to be logged out',
		}
		return render(request, 'register.html', context)
	
	context = {
		'userdata': 'register page',
	}
	return render(request, 'register.html', context)

def login(request):
	context = {}
	return render(request, 'login.html', context)

@login_required(login_url='/admin/')
def profile(request):
	username 	= request.user.username
	user 		= User.objects.get(username=username)
	followers 	= Follower.objects.filter(followed_user=user) #user como seguido
	following 	= Follower.objects.filter(user_follower=user) #user como seguidor
	chats 		= Chatroom.objects.filter(author=username)

	users_followers = []
	users_following = []

	for follower in followers:
		ufwer = follower.user_follower
		users_followers.append(ufwer)
	for followin in following:
		ufwin = followin.followed_user
		users_following.append(ufwin)

	amountFollowers = followers.count()
	amountFollowing = following.count()
	amountChatrooms = chats.count()

	fwers_list 	= followers.all()
	fweds_list 	= following.all()

    for each in chats:
        print(each)

	context  = {
		'userdata': user,
		'followers':amountFollowers,
		'following':amountFollowing,
		'chatrooms':amountChatrooms,
		'frs_list':users_followers,
		'fds_list':users_following,
        'chat_lst':chats,
	}
	return render(request, 'profile.html', context) 

