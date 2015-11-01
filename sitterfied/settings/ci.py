# -*- coding: utf-8 -*-
from .development import *


class MigrationRouter():

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        SQLite cannot handle certain actions so we add an `ignore` key to the
        `hints` dictionary. If `True`, then the migration operation is ignored.

        """
        if hints.get('ignore', False):
            return False

        return True


DEBUG = TEMPLATE_DEBUG = False

CELERY_ALWAYS_EAGER = True

DISABLE_SHORT_URL = True

REDIS_URL = 'redis://'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

STATIC_ROOT = '/tmp/www'

# For testing, use sqlite which will run in-memory
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

DATABASE_ROUTERS = (
    'sitterfied.settings.ci.MigrationRouter',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

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
            'level': 'ERROR',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'boto': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'sitterfied': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
