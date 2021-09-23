from db.models import Message, Chatroom
from asgiref.sync import sync_to_async
import datetime

@sync_to_async
def create_message(message, username, chatroom, time):
	new_message = Message(
		author=username,
		content=message,
		creation_date=time,
		chatroom=chatroom,
		)
	new_message.save()


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