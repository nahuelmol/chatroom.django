from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
	context = {
		'somecontext':'Hellow'
	}
	return render(request, 'index.html', context) 


def room(request, room_name):
	context = {	'room__name':room_name}
	return render(request, 'chatroom.html', context)