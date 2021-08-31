from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from accounts.api.views import LoginView

schema_view = get_swagger_view(title='API name')

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('chat/',   include('chat.urls')),
    path('player/', include(('accounts.api.urls', 'api_name'), namespace='instance_name')),
    path('prove/',  LoginView.as_view()),
    path('api_view/', schema_view)
]
