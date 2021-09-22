from django.contrib.auth import authenticate
from django.shortcuts import render
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from accounts.api.serializers import UserSerializer

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

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer