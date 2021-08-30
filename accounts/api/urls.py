from rest_framework import routers

from accounts.api.views import LoginView, RegisterView

app_name = 'api_name'
#router = routers.SimpleRouter(trailing_slash=False) 
router = routers.DefaultRouter()

login_view		= LoginView
#register_view	= RegisterView.as_view()

router.register(r'login/', 	login_view,	basename='login')
#router.register(r'register/', register_view, basename='register')	

urlpatterns = router.urls