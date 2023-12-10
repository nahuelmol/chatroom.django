import requests
import json
import os

from asgiref.sync import sync_to_async
from dotenv import load_dotenv

from django.contrib.auth.models import User

def compare_message(word, WORD_TO_GUESS):

	if word == WORD_TO_GUESS:
		return True
	else:
		return False

def word_generator():
	load_dotenv()

	apikey 		= os.environ.get('WORD_API_KEY')
	max_length	= str(8)
	min_length	= str(5)
	limit		= str(1)

	try:
		req 	= requests.get('http://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0'
						+'&minLength='+	min_length
						+'&maxLength='+	max_length
						+'&limit='+		limit
						+'&api_key='+	apikey)
		
		if req.status_code == 200:
			result = json.loads(req.content)[0]['word']

			return result

	except Exception as e:
		
		final = '\nit is immposible to create a connection\nword not generated'
		return final


def Msgsender(message, username, time, word):
	msgcontent = ''
	typemsg = ''

	if message == 'winner':
		msgcontent = 'Theres a winner, ' + username + ', the word is: ' + word + '\n'
		typemsg = 'game_noti'

	elif message == 'looser':
		msgcontent = '\n'+username + ' -> failed: ' + word + '\n'
		typemsg = 'word_suggest'

	elif message == 'empty':
		msgcontent = 'theres not a word to guess'
		typemsg = 'game_noti'
		print('generate a word!')

	elif message == 'guess it':
		msgcontent = 'lets try to guess the word'
		typemsg = 'game_noti'

	else:
		msgcontent = 'not a single message'
		typemsg = 'game_noti'

	msg = {	
		'answer':1,
		'message_to_group':msgcontent,
		'user_username_':username,
		'time_of_message':time,
		'type':typemsg
	}

	return msg


async def chatting(username, time, msg):
	admin 	= 0 
	user 	= await sync_to_async(User.objects.get)(username=username)
	
	if user:
		if user.is_staff:
			print(user.username + ' is admin')
			admin = 1
		else:
			admin = 0
			print(user.username + ' is not admin')
	else:
		print(user + ' no existe en la base de datos')

	obj = {
		'admin':admin,
		'message_to_group':msg,
		'user_username_':username,
		'time_of_message':time,
		'type':'chat_msg'
	}

	return obj

def command(word, user, frase, time):

	msgcontent = ''
	pabs 	= frase.split()[:1]
	cmd 	= pabs[0]

	typemsg = ''

	if cmd == 'generate':
		msgcontent = 'lets try to guess the word'

		WORD_TO_GUESS = word_generator()
		word.change(WORD_TO_GUESS)

		print("the word is ", WORD_TO_GUESS)
		typemsg = 'game_noti'

	elif cmd == 'ban':
		pabs 	= frase.split()[:4]
		userbanned = pabs[1]
		typemsg = 'banned'
		msgcontent = 'The user ' + userbanned+ 'has been banned for ' + pabs[2] + pabs[3]

	elif cmd == 'fix':
		msgcontent = 'message has been fixed'

	elif cmd == 'resp':
		pabs 	= frase.split()[:2]
		msgcontent = 'responding to ' + pabs[1]

	elif cmd == 'like':
		msgcontent = 'liking message'

	msg = {	
		'answer':1,
		'message_to_group':msgcontent,
		'user_username_':user,
		'time_of_message':time,
		'type':typemsg
	}


	return msg
	
