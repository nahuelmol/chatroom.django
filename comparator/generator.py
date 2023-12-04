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

	

	

if __name__ == "__main__":
	word_generator()
