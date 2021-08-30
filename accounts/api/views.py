from django.contrib.auth import authenticate
from django.shortcuts import render
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User

class LoginView(APIView):

	@classmethod
	def get_extra_actions(cls):
		return []

	def post(self, request, format=None):

		u_name 	= request.data.get('username')
		p_word 	= request.data.get('password')
		user 	= authenticate(username=u_name, password=p_word)
		if user:
			return Response({'token':user.auth_token.key})
		else:
			return Response({'error':'wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
	def post(self, request,):
		permission_class()

		u_name 	= request.data.get('username')
		p_word	= request.data.get('password')
		email 	= request.data.get('email')

		user = User(
			email 		= email,
			username	= u_name
			)
		user.set_password(p_word)
		user.save()

		Token.objects.create(user=user)

		return redirect('login')