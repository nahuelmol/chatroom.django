import json
import datetime

from channels.generic.websocket import AsyncWebsocketConsumer
from comparator.generator import word_generator

from db.views import create_message
from comparator.generator import compare_message, word_generator
from comparator.generator import Msgsender, chatting, command
from comparator.generator import BanningPeople, ModeratingPeople

from asgiref.sync import sync_to_async


class Word:
	def __init__(self, word):
		self._word = word

	def change(self, neword):
		self._word = neword

	def clean(self):
		self._word = ' '

class Counter:
	def __init__(self,count):
		self._count = count

	def monitor(self):
		print('users connected: '+ str(self._count))

	def more(self):
		self._count = self._count + 1

	def less(self):
		self._count = self._count - 1     

######################################################################################

my_counter = Counter(0)
word = Word(' ')

class ChatRoomConsumer(AsyncWebsocketConsumer):

	async def connect(self):
		
		my_counter.more()
		my_counter.monitor()

		self.room_name 			= self.scope['url_route']['kwargs']['room_name']
		self.room_group_name	='chat_%s' % self.room_name

		print('you are connected to '+' '+self.room_group_name+' room group')
		
		await self.channel_layer.group_add (
			self.room_group_name,
			self.channel_name
			)
		await self.accept()

		await self.channel_layer.group_send(self.room_group_name,
			{	'type':'welcome_message',
				'tester':'Welcome to the Chat Room',
				'connected': my_counter._count})

	async def welcome_message(self, event):
		tester 						= event['tester'] #capturing the value
		await self.send(text_data 	= json.dumps({'tester':tester})) #sending the value

	######################################################################

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
			)
		my_counter.less()
		my_counter.monitor()

	######################################################################
	async def receive(self, text_data):
		text_data_json	= json.loads(text_data)
		result 			= datetime.datetime.now()

		message 		= text_data_json['message']
		username		= text_data_json['username']
		email			= text_data_json['email']
		time			= str(result.hour) +':'+str(result.minute)

		await create_message(message, username, self.room_group_name, time)

		obj = {
			'type':'chatroom_message',
			'message_event':message,
			'username_event':username,
			'time_event':time}

		await self.channel_layer.group_send(self.room_group_name, obj)

	async def chatroom_message(self, event):

		message 		= event['message_event'] #we collect the message event from the group (inside of receive function)
		user_username 	= event['username_event'] #we collect the username too
		time_message 	= event['time_event']



		if message[0] == '#':
			
			if word._word != ' ':
				word_msg = message.replace('#',"")
				res = compare_message(word_msg, word._word)

				if res:
					msg = Msgsender('winner', user_username, time_message, word._word)
					print('well done!')
				else:
					msg = Msgsender('looser', user_username, time_message, word_msg)
					print('failed!')


				await self.send(text_data=json.dumps(msg))

			else:
				msg = Msgsender('empty', user_username, time_message, word._word)
				await self.send(text_data=json.dumps(msg))

		elif message[0] == '!':

			frase 	= message.replace('!',"")

			msg = command(word, user_username, frase, time_message)

			await self.send(text_data=json.dumps(msg))

		elif message[0] == '@':

			which  = message.replace('@', "")

			if which == 'ban':

				msg = await BanningPeople(user_username, time_message)

			if which == 'mod':

				msg = await ModeratingPeople(user_username, time_message)

			await self.send(text_data=json.dumps(msg))

		else:
			msg = await chatting(user_username, time_message, message)
			await self.send(text_data=json.dumps(msg))

		people = {
			'countered':my_counter._count
		}

		await self.send(text_data=json.dumps(people))

	###########################################################
	pass
