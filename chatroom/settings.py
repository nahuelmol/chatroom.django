from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '9i03(slfzo^4%=si+$1wi_9aq_c1jfbspo8t2vjgthwg4ef28z'

DEBUG = True

ALLOWED_HOSTS = ['192.168.0.103','localhost','192.168.1.38']
CHANNELS_ALLOWED_HOSTS = ['localhost', '192.168.1.38']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",  # Agrega tu dirección IP o nombre de dominio aquí
    "http://192.168.1.38:3000",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'channels',
    'chat',
    #'comparator',
    #'mytests',
    'db',
    'accounts',
    'drf_yasg',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'chatroom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('D:/python-backend/chatroom/chat', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chatroom.wsgi.application'
ASGI_APPLICATION = 'chatroom.routing.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE   = 'en-us'

TIME_ZONE       = 'UTC'

USE_I18N        = True

USE_L10N        = True

USE_TZ          = True

STATIC_URL      = '/static/'

CHANNEL_LAYERS  = {
    "default":{ "BACKEND":"channels.layers.InMemoryChannelLayer"}
    }


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':{
        #'rest_framework.authentication.TokenAuthentication',
        #'rest_framework.authentication.SessionAuthentication'
    },
    'DEFAULT_PERMISSION_CLASSES':{
        'rest_framework.permissions.IsAuthenticated'
    }
}
