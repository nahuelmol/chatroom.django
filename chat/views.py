from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse

from rest_framework.authtoken.models import Token
from rest_framework import authentication

from itertools import chain

from db.models import Chatroom, Message, Follower, Subscriber
from db.views import create_chatroom
from accounts.utils import token_required

def about(request):
    context = {}
    return render(request, 'about.html', context)

def register(request):
    context = {}
    return render(request, 'register.html', context)

@token_required
def create(request):
    context = {}
    return render(request, 'create.html', context)

@login_required(login_url='accounts:login')
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

@token_required
def room(request, name):
    array       = []
    msg_array 	= []
    queryset 	= []

    is_owner 	= False
    is_follower = False
    is_subscriber = False

    token = request.COOKIES.get("access_token")
    if token:
        tokn = Token.objects.get(key=token)
        user = tokn.user
        USERlogged 		= User.objects.get(username=user.username)

    CHATROOM 		= Chatroom.objects.get(chatroom_name=name)
    USERowner 		= User.objects.get(username=CHATROOM.author)

    followerREL 	= Follower.objects.filter(user_follower=USERlogged)
    subscriberREL 	= Subscriber.objects.filter(follower_subscriber=USERlogged)

    for each in followerREL:
        if(each.followed_user == USERowner):
            print('the current user is follower of the current chat')
            is_follower = True

    for each in subscriberREL:
        if(each.subscribed_use == USERowner):
            print('the current user is subscriber of the current chat')
            is_subscriber = False

    for each in Chatroom.objects.all():
        array.append(each.chatroom_name)

    if not (name in array):
        return redirect('chatviews:about')

    for each in Message.objects.all():
        if each.chatroom == 'chat_'+ name:
            msg_array.append(each)

    if (user.username == CHATROOM.author):
        is_owner = True

    context = {	'room__name':name,
                'messages':msg_array,
                'is_owner':is_owner,
                'is_follower':is_follower,
    }

    return render(request, 'chatroom.html', context)

def explore(request):
    context = {}
    return render(request, 'explore.html', context) 

