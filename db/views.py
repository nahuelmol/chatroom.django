from db.models import Message, Chatroom, Event, Subscriber
from asgiref.sync import sync_to_async
import datetime

from django.shortcuts import redirect

@sync_to_async
def create_message(message, username, chatroom, time):
	new_message = Message(
		author=username,
		content=message,
		creation_date=time,
		chatroom=chatroom,
		)
	new_message.save()

@sync_to_async
def add_user_subscribed(req,chatroom,usubscribed,dsubscribed):
	new_subscriber = Subscriber(
		user_subscribed=usubscribed,
		creation_date=dsubscribed,
		chatroom=chatroom)

	new_subscriber.save()

@sync_to_async
def encuesta():

	new_encuesta = Encuesta(
		author=username,
		options=options,
		creation_date=time,
		chatroom=chatroom
		)

	new_encuesta.save()

def create_event(username, chatroom, texto, time, deadline):

	result 			= datetime.datetime.now()
	time			= str(result.hour) +':'+str(result.minute)


	new_event = Event(
		author=username,
		content=texto,
		creation_date=time,
		chatroom=chatroom,
		location=location,
		is_invited=is_invited,
		deadline=deadline
		)

	new_event.save()


def create_chatroom(chatroom_name,author):

	result 			= datetime.datetime.now()
	time			= str(result.hour) +':'+str(result.minute)
	link 			= "http://localhost:8000"+"/"+chatroom_name

	new_chat = Chatroom(
		chatroom_name=chatroom_name,
		creation_date=time,
		author=author,
		link_to_join=link,
		)

	new_chat.save()

	if(new_chat):
		return redirect(link)