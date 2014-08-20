# -*- coding: utf-8 -*-
from .base import *
from .mandrill import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.100.22',
)


# ShortUrl Redis Configuration
REDIS_URL = 'redis://192.168.100.22:6379'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sitterfied',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '192.168.100.22',
        'PORT': '',
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child("media")
MEDIA_URL = "/media/"


GOOGLE_OAUTH_CLIENT_ID = '213296649304-10d5ppglkmjmq7l60uub4r5nvnklfjoa.apps.googleusercontent.com'
GOOGLE_OAUTH_CLIENT_SECRET = 'u9BePfC9OC9Z3XkO0SMJbwkq'
GOOGLE_OAUTH_REDIRECT_URI = "http://sitterfied.ngrok.com"


# Override Short URL
SHORT_URL = 'localhost:8000/'

# Override Twilio Settings
TWILIO_DEFAULT_CALLERID = '+19088384816'

# Override Facebook App ID
FACEBOOK_APP_ID = '746551758706532'


# Celery configuration
BROKER_URL = REDIS_URL + '/0'
