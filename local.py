from waitress import serve
from chatroom.wsgi import application

if __name__ == '__main__':
	serve(application, host='192.168.0.103',port='8080')