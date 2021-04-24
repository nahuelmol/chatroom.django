import json

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.room_name 			= self.scope['url_route']['kwargs']['room_name']
		self.room_group_name	='chat_%s' % self.room_name

		await self.channel_layer.group_add (
			self.room_group_name,
			self.channel_name
			)
		await self.accept()

		#await self.channel_layer.group_send (
		#	self.room_group_name,
		#	{'type':'tester_message','tester':'hello world'}
		#	)
	#async def tester_message(self, event):
	#	tester 						= event['tester'] #capturing the value
	#	await self.send(text_data 	= json.dumps({'tester':tester})) #sending the value

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
			)


	async def receive(self, text_data):
		text_data_json	= json.loads(text_data)
		message 		= text_data_json['message']
		username		= text_data_json['username']

		await self.channel_layer.group_send (
			self.room_group_name,
			{'type':'chatroom_message','message':message,'username':username}
			)

	async def chatroom_message(self, event):
		message = event['message'] #we collect the message event from the group (inside of receive function)
		user_username = event['username'] #we collect the username too

		#then we send the info
		await self.send(text_data=json.dumps({
			'message':message,
			'user_username':user_username
			}))
	

	pass