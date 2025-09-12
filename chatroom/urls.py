from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.api.views import LoginView

schema_view = get_schema_view(
        openapi.Info(
            title='API name',
            default_version='v1',
            description="API description",
            terms_of_service="https://www.example.com",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/',  	admin.site.urls),

    path('player/', 	include(('accounts.urls'), namespace='accounts')),
    path('player/api/', include(('accounts.api.urls', 'accountapi'), namespace='instance_name')),

    path('chat/',   	include('chat.urls', namespace='chatviews')),
    path('chat/api/',   include(('chat.api.urls', 'chatapi'), namespace='instance_name')),

    path('db/', 		include('db.api.urls')),
    path('swagger/', 	schema_view.with_ui('swagger', cache_timeout=0), name='schema-swg-ui'),
]
