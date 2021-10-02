from rest_framework import routers

from accounts.api.views import LoginView, UserViewSet, UserLogout, RegisterView
from django.urls import include, path

from rest_framework.authentication import TokenAuthentication

app_name = 'api_name'
router = routers.SimpleRouter()

login_view		= LoginView.as_view()
logout_view 	= UserLogout.as_view()
register_view 	= RegisterView.as_view()

urlpatterns = [
	path('login/',		login_view),
	path('logout/',		logout_view),
	path('register/',	register_view)
]

urlpatterns += router.urls