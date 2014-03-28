# -*- coding: utf-8 -*-
from .base import *
from .mandrill import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.111.1',
)


# ShortUrl Redis Configuration
REDIS_URL = 'redis://localhost:6379'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sitterfied',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_ROOT.child("media")
MEDIA_URL = "/media/"


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.child("static_source"),  # An absolute path: /foo/bar/baz.py
)


GOOGLE_OAUTH_CLIENT_ID = '213296649304-10d5ppglkmjmq7l60uub4r5nvnklfjoa.apps.googleusercontent.com'
GOOGLE_OAUTH_CLIENT_SECRET = 'u9BePfC9OC9Z3XkO0SMJbwkq'
GOOGLE_OAUTH_REDIRECT_URI = "http://sitterfied.ngrok.com"

INSTALLED_APPS += (
    #'debug_toolbar',
    'devserver',
)

MIDDLEWARE_CLASSES += (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}


DEVSERVER_ARGS = ['--werkzeug']


DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
)


DEVSERVER_AUTO_PROFILE = True


# Override Short URL
SHORT_URL = 'localhost:8000/'

# Override Twilio Settings
TWILIO_DEFAULT_CALLERID = '+19088384816'

# Override Facebook App ID
FACEBOOK_APP_ID = '746551758706532'


# Celery configuration
BROKER_URL = REDIS_URL + '/0'
