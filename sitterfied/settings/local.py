# -*- coding: utf-8 -*-
from .base import *
from .mandrill import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = (
    '::1',
    '127.0.0.1',
    '192.168.100.1',
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

STATIC_ROOT = "/www/static"

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
BROKER_TRANSPORT_OPTIONS = {
    # Set visibility timeout to 1 year, this is necessary to prevent
    # celery from executing scheduled celery tasks multiple times.
    'visibility_timeout': 31536000,
}

# Whether the Query Inspector should do anything (default: False)
QUERY_INSPECT_ENABLED = True
# Whether to log the stats via Django logging (default: True)
QUERY_INSPECT_LOG_STATS = True
# Whether to add stats headers (default: True)
QUERY_INSPECT_HEADER_STATS = True
# Whether to log duplicate queries (default: False)
QUERY_INSPECT_LOG_QUERIES = True
# Whether to log queries that are above an absolute limit (default: None - disabled)
QUERY_INSPECT_ABSOLUTE_LIMIT = 100  # in milliseconds
# Whether to log queries that are more than X standard deviations above the mean query time (default: None - disabled)
QUERY_INSPECT_STANDARD_DEVIATION_LIMIT = 2
# Whether to include tracebacks in the logs (default: False)
QUERY_INSPECT_LOG_TRACEBACKS = True
# Project root (one or several colon-separated directories, default empty)
QUERY_INSPECT_TRACEBACK_ROOTS = ['./']
