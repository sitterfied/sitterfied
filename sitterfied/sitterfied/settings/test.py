# -*-coding: utf-8 -*-
import os
import json

from .base import *
from .mandrill import *

with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

DEBUG = False

# ShortUrl Redis Configuration
REDIS_URL = env.get('DOTCLOUD_CACHE_REDIS_URL')


# Celery Configuration
BROKER_URL = REDIS_URL + '/0'


# Django Configuration
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': env.get('DOTCLOUD_CACHE_REDIS_HOST', '') + ":" + env.get('DOTCLOUD_CACHE_REDIS_PORT', ''),
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': env.get('DOTCLOUD_CACHE_REDIS_PASSWORD', ''),
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'PICKLE_VERSION': 2,
        },
    },
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sitterfied',
        'USER': env.get('DOTCLOUD_DATA_SQL_LOGIN', ''),
        'PASSWORD': env.get('DOTCLOUD_DATA_SQL_PASSWORD', ''),
        'HOST': env.get('DOTCLOUD_DATA_SQL_HOST', ''),
        'PORT': int(env.get('DOTCLOUD_DATA_SQL_PORT', '0')),
    }
}


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = "/home/dotcloud/data/media/"


MIDDLEWARE_CLASSES += (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)


# Google OAuth Configuration
GOOGLE_OAUTH_CLIENT_ID = '305141264963-9gamu3g0ja74ch7pcssmmk75shtk9ftc.apps.googleusercontent.com'
GOOGLE_OAUTH_CLIENT_SECRET = 'LSeO2JmrERhe_vRNUFnVsfuc'
GOOGLE_OAUTH_REDIRECT_URI = 'http://test.sitterfied.com'


# Override URL Shortening
SHORT_URL = 'test.sttrfd.us/'


# Override Popcorn Metrics ID
POPCORN_METRICS_ID = '53f62873ed69ca02000003ef'


# Override Twilio Configuration
TWILIO_DEFAULT_CALLERID = '+19088384816'


# Override Facebook App ID
FACEBOOK_APP_ID = '624946094225118'


try:
    JOB_FIRST_REMINDER = int(env.get('JOB_FIRST_REMINDER'))
    JOB_SECOND_REMINDER = int(env.get('JOB_SECOND_REMINDER'))
    JOB_RELIEF_REMINDER = int(env.get('JOB_RELIEF_REMINDER'))
except:
    pass


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/var/log/supervisor/application.log',
            'maxBytes': 1024 * 1024 * 25,  # 25 MB
            'backupCount': 5,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
