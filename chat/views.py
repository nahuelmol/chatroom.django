from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from db.models import Chatroom
from db.views import create_chatroom

@login_required(login_url='/accounts/login/')
def index(request):
	chat_list = Chatroom.objects.all()

	context = {
		'chat_list': chat_list
	}
	return render(request, 'index.html', context) 


def room(request, room_name):
	context = {	'room__name':room_name}
	array = []

	for each in Chatroom.objects.all():
		array.append(each.chatroom_name)

	if not (room_name in array):
		create_chatroom(room_name, request.user)

	return render(request, 'chatroom.html', context)