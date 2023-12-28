from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from accounts.api.views import LoginView

schema_view = get_swagger_view(title='API name')

urlpatterns = [
    path('admin/',  	admin.site.urls),
    
    path('chat/',   	include('chat.urls', namespace='chatapp')),
    path('create/',		include('chat.api.urls', namespace='saver')),

    path('player/', 	include(('accounts.api.urls', 'accountapp'), namespace='instance_name')),
    path('prove/',  	LoginView.as_view()),
    path('db/', 		include('db.api.urls')),
    path(r'api_docs/', 	schema_view),

]
