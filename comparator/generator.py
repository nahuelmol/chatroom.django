import requests
import json

from dotenv import load_dotenv

def word_generator():
	load_dotenv()

	apikey 		= os.environ.get('WORD_API_KEY')
	max_length	= 8
	min_length	= 5
	limit		= 1

	req 	= requests.get('http://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0'
						+'&minLength='+	min_length
						+'&maxLength='+	max_length
						+'&limit='+		limit
						+'&api_key='+	apikey)

	if req.status_code == 200:
		result = json.loads(req.content)[0]['word']

		return result

if __name__ == "__main__":
	word_generator()
