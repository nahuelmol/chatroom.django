from django.contrib.auth import authenticate
from django.shortcuts import render
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework import authentication, permissions

from accounts.api.serializers import UserSerializer
from accounts.utils import generate_access_token

from django.contrib.auth.models import User

class LoginView(APIView):
	authentication_classes = [
		authentication.TokenAuthentication]

	permission_classes = [
		permissions.AllowAny]

	@classmethod
	def get_extra_actions(cls):
		return []

	def post(self, request, format=None):

		u_name 	= request.data.get('username')
		p_word 	= request.data.get('password')
		headers = request.META

		user 	= authenticate(username=u_name, password=p_word)
		if user:
			messages.success(request, 'logged in')
			user_access_token = generate_access_token(user)

			if user_access_token:
				response = redirect(headers.get('HTTP_REFERER', '/'))
				response.set_cookie(key='access_token', value=user_access_token,httponly=True)
				return response

			response = redirect(headers.get('HTTP_REFERER'),'/')
			messages.add_message(request, messages.INFO, 'cannot be created a token for the user')
			return response
		else:
			messages.error(request, 'not a user to log in')
			response = redirect(headers.get('HTTP_REFERER', '/'),status=status.HTTP_400_BAD_REQUEST)
			return response

class RegisterView(APIView):
	authentication_classes = [
		authentication.TokenAuthentication]
	permission_classes = [
		permissions.AllowAny]

	def post(self, request):
		headers 	= request.META
		email_ 		= request.data.get('email')
		username_ 	= request.data.get('username')
		pass_ 		= request.data.get('password')

		new_user = User(
				email=email_,
				username=username_
				)
		new_user.set_password(pass_)
		new_user.save()

		if new_user:
			access_token = generate_access_token(new_user)
			if access_token:
				response = redirect(headers.get('HTTP_REFERER', '/'))
				response.set_cookie(key='access_token', value=access_token)
				response.data = {'access_token': 'created'}
		
				return response
			else:
				response = redirect(headers.get('HTTP_REFERER', '/'))
				response.data = {'access_token':'was not created'}
				return response
		else:
			response = redirect(headers.get('HTTP_REFERER', '/'))
			response.data = {'user':'there is no such user'}
			return response

class UserLogout(APIView):
	authentication_classes 	= [
		authentication.TokenAuthentication]
	permission_classes 		= [
		permissions.AllowAny]

	def get(self, request):

		user_token  = request.COOKIES.get('access_token', None)
		headers 	= request.META

		if user_token:
			response = redirect(headers.get('HTTP_REFERER', '/login'))
			response.delete_cookie('access_token')
			messages.success(request, 'logged out successfully')
			return response 
		response = redirect(headers.get('HTTP_REFERER', '/homepage'))
		messages.success(request, 'you are already logged out')
		return response

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer