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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'ignore_http_header': {
            '()': 'sitterfied.utils.log.IgnoreRegularExpressionFilter',
            'pattern': r'^Invalid HTTP_HOST header',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
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
            'filename': '/var/log/sitterfied/application.log',
            'maxBytes': 1024 * 1024 * 25,  # 25 MB
            'backupCount': 5,
        },
        'mail_admins': {
            'filters': ['ignore_http_header', 'require_debug_false'],
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'ERROR',
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
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
