from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
            user_access_token = generate_access_token(user)
            if user_access_token:
                response = redirect('chatviews:create')
                response.set_cookie(key='access_token', value=user_access_token, httponly=True)
                defaults = { "key":user_access_token }
                obj, created = Token.objects.update_or_create(user=user, defaults=defaults)
                return response

            response = redirect('chatviews:login')
            return response
        else:
            response = redirect('chatviews:login', status=status.HTTP_400_BAD_REQUEST)
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
                response = redirect('chatviews:create')
                response.set_cookie(key='access_token', value=access_token)
                defaults = { "key":user_access_token }
                obj, created = Token.objects.update_or_create(user=new_user, defaults=defaults)
                return response
            else:
                response = redirect('chatviews:register')
                return response
        else:
            response = redirect('chatviews:register')
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
            response = redirect('chatviews:login')
            response.delete_cookie('access_token')
            return response
        else:
            return redirect('chatviews:about')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
