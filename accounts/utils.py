from django.conf import settings
from django.shortcuts import redirect
from functools import wraps
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

import jwt

def generate_access_token(user):
	payload = {
		'user_id':user.id,
	}

	access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
	return access_token

def token_required(view):
    @wraps(view)
    def wrapped_view(request, *args, **kwargs):
        token = request.COOKIES.get("access_token")
        if not token:
            res = {
                "error":"Authentication credentials were not provided"
            }
            return redirect('accounts:login')
        try:
            token_ = Token.objects.get(key=token)
            request_user = token_.user
        except Token.DoesNotExist:
            res = {
                "error":"invalid token"
            }
            return redirect('accounts:login')
        return view(request, *args, **kwargs)
    return wrapped_view
