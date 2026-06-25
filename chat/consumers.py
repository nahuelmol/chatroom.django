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

        self.room_name          = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name    ='chat_%s' % self.room_name

        print('you are connected to '+' '+self.room_group_name+' room group')
        
        await self.channel_layer.group_add (
            self.room_group_name,
            self.channel_name
            )
        await self.accept()
        await self.channel_layer.group_send(self.room_group_name,
            {   'type':'welcome_message',
                'tester':'Welcome to the Chat Room',
                'connected': my_counter._count})

    async def welcome_message(self, event):
        tester                      = event['tester'] #capturing the value
        await self.send(text_data   = json.dumps({'tester':tester})) #sending the value

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
        json_data   = json.loads(text_data)
        now         = datetime.datetime.now()
        time        = str(now.hour) +':'+str(now.minute)

        if "type" in json_data:
            if json_data["type"] == "typing":
                await self.channel_layer.group_send(
                    self.room_group_name,
                        {
                            "type": "typing_event",
                            "typing": json_data["typing"],
                            "username": self.scope["user"].username,
                        })

            elif json_data["type"] == "message":
                message     = json_data['message']
                username    = json_data['username']
                email       = json_data['email']

                await create_message(message, username, self.room_group_name, time)

                obj = { 'type':'chatroom_message',
                        'message_event':message,
                        'username_event':username,
                        'time_event':time}
                await self.channel_layer.group_send(self.room_group_name, obj)
            else:
                print("not recognized type")
        else:
            print("message has not type")

    async def typing_event(self, event):
        await self.send(text_data=json.dumps({
            "type": "typing",
            "typing": event["typing"],
            "username": event["username"],
        }))
    
    async def chatroom_message(self, event):
        message         = event['message_event']
        user_username   = event['username_event'] 
        time_message    = event['time_event']
        msg = ''
        if len(message) == 0:
            print('message is not valid')
            return
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
            else:
                msg = Msgsender('empty', user_username, time_message, word._word)
            await self.send(text_data=json.dumps(msg))

        elif message[0] == '!':
            frase   = message.replace('!',"")
            msg     = command(word, user_username, frase, time_message)
            await self.send(text_data=json.dumps(msg))

        elif message[0] == '@':
            which  = message.replace('@', "")
            if which == 'ban':
                msg = await BanningPeople(user_username, time_message)
            elif which == 'mod':
                msg = await ModeratingPeople(user_username, time_message)
            else:
                msg = await chatting(user_username, time_message, message)
                await self.send(text_data=json.dumps(msg))

            await self.send(text_data=json.dumps(msg))

        else:
            msg = {
                'type':'chat_msg',
                'message':message,
                'username':user_username,
                'time':time_message
            }
            await self.send(text_data=json.dumps(msg))

        people = {
            'countered':my_counter._count
        }

        await self.send(text_data=json.dumps(people))
        
    ###########################################################
    pass


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected to notification consumer')
        await self.accept()

    async def disconnect(self, close_code):
        print('disconnected')

    async def receive(self, text_data):
        data        = json.loads(text_data)
        now         = datetime.datetime.now()
        message     = data['message']
        username    = data['username']
        email       = data['email']
        time        = str(now.hour) +':'+str(now.minute)

        if data["type"] == "invite_user":
            await channel_layer.group_send(
                f"user_{user_b.id}",
                {
                    "type": "chat_invitation",
                    "chat_id": self.chat.id,
                    "chat_name": self.chat.name,
                    "from": self.scope["user"].username,
                }
            )
        else:
            print("not inviting")

    async def chat_invitation(self, event):

        await self.send(text_data=json.dumps({
            "type": "chat_invitation",
            "chat_id": event["chat_id"],
            "chat_name": event["chat_name"],
            "from": event["from"],
        }))

    pass
