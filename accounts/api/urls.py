from rest_framework import routers

from accounts.api.views import LoginView, UserViewSet
from django.urls import include, path

from rest_framework.authentication import TokenAuthentication

app_name = 'api_name'
#router = routers.SimpleRouter(trailing_slash=False) 
router = routers.SimpleRouter()

login_view		= LoginView.as_view()

router.register('users', UserViewSet)
#router.register(r'login/', 	login_view,	basename='login')

urlpatterns = [
	path('login/',	login_view),
]

urlpatterns += router.urls