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
			'userdata': 'you need to be logged out',
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

