from django.contrib import admin
from django.urls import path, include

from accounts.api.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('player/', include(('accounts.api.urls', 'api_name'), namespace='instance_name')),
    path('prove/', LoginView.as_view())
]
