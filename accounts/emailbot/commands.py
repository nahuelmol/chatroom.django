from .start import create_message_with_attachment, get_service, send_message

def verification_account():
	service = get_service()
	user_id = 'me'
	sender = 'molinahuel44@gmail.com'
	to = destino  
	subject = 'please verify your account!'
	body = mystring
	file = 'bot/sample.txt'
    
	msg = create_message_with_attachment(sender,to,subject,body,file)
	send_message(service,user_id,msg)
