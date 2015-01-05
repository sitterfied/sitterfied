# -*-coding: utf-8 -*-
from .deployed import *

from kombu import Exchange, Queue

SESSION_COOKIE_NAME = 'sitterfied-test'

ELASTICACHE_ENDPOINT = 'website-test.ug6jhv.0001.use1.cache.amazonaws.com:6379'

# ShortUrl Redis Configuration
REDIS_URL = 'redis://{}'.format(ELASTICACHE_ENDPOINT)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': ELASTICACHE_ENDPOINT,
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'PICKLE_VERSION': 2,
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sitterfied',
        'USER': 'sitterfied',
        'PASSWORD': '^uM*e3xj79eFLrc',
        'HOST': 'website-test-website-server-database.cd92rfe8vffs.us-east-1.rds.amazonaws.com',
        'PORT': 5432,
    }
}

CELERY_DEFAULT_QUEUE = 'sitterfied-test'
CELERY_QUEUES = (
    Queue(CELERY_DEFAULT_QUEUE, Exchange(CELERY_DEFAULT_QUEUE, routing_key=CELERY_DEFAULT_QUEUE)),
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

# Override Sideswipe.io Token
SIDESWIPE_IO_TOKEN = 'd647eccfe96499d0f8aa85a7f96a2cd5'
