from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from db.models import Chatroom, Message
from db.views import create_chatroom

@login_required(login_url='/admin/')
def index(request):
	chat_list = Chatroom.objects.all()

	context = {
		'chat_list': chat_list
	}
	return render(request, 'index.html', context) 

def algo(request):
	print("hola")

	return HttpResponse("Hola")


def create_new_chat(request):

	print(request.method)
	print(request.status_code)

	if request.method == 'POST':
		chatname 	= request.data.get('chatname')
		author 		= request.data.get('author')

		print(chatname)
		print(author)

		create_chatroom(chatname, author)
	else:
		print("nothing")
	
	return redirect('/admin/')

def room(request, room_name):
	array = []
	msg_array = []

	for each in Chatroom.objects.all():
		array.append(each.chatroom_name)

	if not (room_name in array):
		return redirect('chatapp:index')

	for each in Message.objects.all():
		if each.chatroom == 'chat_'+ room_name:
			msg_array.append(each)

	context = {	'room__name':room_name,
				'messages':msg_array
		}

	return render(request, 'chatroom.html', context)