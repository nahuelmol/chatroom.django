from waitress import serve
from chatroom.wsgi import application
from dotenv import load_dotenv

import os
import socket

load_dotenv()
ENV  = os.getenv('ENVIRONMENT')
HOST = ''
PORT = os.getenv('PORT')

print('env: ', ENV)
if ENV == 'development':
    HOST = socket.gethostbyname(socket.gethostname()) 
    print('on host: {}:{}'.format(HOST, PORT)) 
elif ENV == 'production':
    HOST = os.getenv('IPADRESS')
    print('on host: {}:{}'.format(HOST, PORT))
else:
    print('IPADRESS not setted')

if __name__ == '__main__':
	serve(application, host=HOST, port=PORT)
