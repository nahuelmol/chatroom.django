import json
import datetime

from channels.generic.websocket import AsyncWebsocketConsumer
from comparator.generator import word_generator

from db.views import create_message
from comparator.generator import compare_message, word_generator

from asgiref.sync import sync_to_async


class Counter:
	def __init__(self,count):
		self._count = count

	def monitor(self):
		print('users connected: '+ str(self._count))

	def more(self):
		self._count = self._count + 1

	def less(self):
		self._count = self._count - 1     

my_counter = Counter(0)

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

		await self.channel_layer.group_send (self.room_group_name,
			{	'type':'welcome_message',
				'tester':'Welcome to the Chat Room'})

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

		print('time: '+time)

		await self.channel_layer.group_send (
			self.room_group_name,
			{'type':'chatroom_message','message_event':message,'username_event':username,'time_event':time}
			)

	async def chatroom_message(self, event):

		global WORD_TO_GUESS

		message 		= event['message_event'] #we collect the message event from the group (inside of receive function)
		user_username 	= event['username_event'] #we collect the username too
		time_message 	= event['time_event']

		if message[0] == '#':
			word_msg = message.replace('#',"")
			res = compare_message(word_msg, WORD_TO_GUESS)

			if res:
				await self.send(text_data=json.dumps({
					'message_to_group':'Theres a winner, ' + 
						user_username + ', the word is: ' +
						word_msg + '\n',
					'user_username_':'computer',
					'time_of_message':time_message
					}))

				print('well done!')
			else:
				print('failed')

			print(word_msg)

		if message == 'generate':

			await self.send(text_data=json.dumps({
					'message_to_group':'lets try to guess the word\n',
					'user_username_':'computer',
					'time_of_message':time_message
					}))

			WORD_TO_GUESS = word_generator()
			print(WORD_TO_GUESS)

		#then we send the info
		await self.send(text_data=json.dumps({
			'message_to_group':message,
			'user_username_':user_username,
			'time_of_message':time_message
			}))
	###########################################################

	pass
