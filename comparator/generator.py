import requests
import json
import os

from asgiref.sync import sync_to_async

from dotenv import load_dotenv

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

	if message == 'winner':
		msgcontent = 'Theres a winner, ' + username + ', the word is: ' + word + '\n'

	elif message == 'looser':
		msgcontent = username + 'failed with: ' + word + '\n'

	elif message == 'generate':
		msgcontent = 'generate a word!'

	elif message == 'empty':
		msgcontent = 'theres not a word to guess'

	elif message == 'guess it':
		msgcontent = 'lets try to guess the word'

	else:
		msgcontent = 'not a single message'

	msg = {	'answer':1,
		'message_to_group':msgcontent,
		'user_username_':'computer',
		'time_of_message':time
	}

	return msg


def chatting(user, time, msg):
	
	obj = {
		'answer':1,
		'message_to_group':msg,
		'user_username_':'computer',
		'time_of_message':time
	}

	return obj