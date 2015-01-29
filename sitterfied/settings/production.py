# -*- coding: utf-8 -*-
from .deployed import *

from kombu import Exchange, Queue

SESSION_COOKIE_NAME = 'sitterfied-prod'

ELASTICACHE_ENDPOINT = 'website-prod-001.ug6jhv.0001.use1.cache.amazonaws.com:6379'

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
        'PASSWORD': 'XXcCBqyRsHWA3D2',
        'HOST': 'website-prod-website-server-database.cd92rfe8vffs.us-east-1.rds.amazonaws.com',
        'PORT': 5432,
    }
}

BROKER_TRANSPORT_OPTIONS.update(queue_name_prefix='prod-')
CELERY_DEFAULT_QUEUE = 'sitterfied-prod'
CELERY_QUEUES = (
    Queue(CELERY_DEFAULT_QUEUE, Exchange(CELERY_DEFAULT_QUEUE, routing_key=CELERY_DEFAULT_QUEUE)),
)

# Google OAuth Config
GOOGLE_OAUTH_CLIENT_ID = '305141264963-9av2onc3pdada6mtkat6uorhv99k5nhu.apps.googleusercontent.com'
GOOGLE_OAUTH_CLIENT_SECRET = 'rwUoSO0hjvtL5ZtOqznzL5WB'
GOOGLE_OAUTH_REDIRECT_URI = 'http://www.sitterfied.com'

# Knowtify Config
KNOWTIFY_API_TOKEN = 'eeaf1c3b2d47247cc401a3e7dc9162b5'

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
            'level': 'INFO',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'log_file': {
            'level': 'INFO',
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
            'email_backend': 'django_ses.SESBackend',
        },
    },
    'loggers': {
        'boto': {
            'handlers': ['console', 'log_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
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
