# -*- coding: utf-8 -*-
from celery.schedules import crontab
from kombu import Exchange, Queue

from .base import *
from .test.facebook import *
from .test.google import *
from .test.hellobar import *
from .test.intercom import *
from .test.knowtify import *
from .test.mandrill import *
from .test.segment import *
from .test.sideswipeio import *
from .test.twilio import *
from .test.uploadcare import *

DEBUG = TEMPLATE_DEBUG = True

SESSION_COOKIE_NAME = 'sitterfied-dev'

INTERNAL_IPS = (
    '::1',
    '127.0.0.1',
    '192.168.100.1',
)

# ShortUrl Redis Configuration
REDIS_URL = 'redis://127.0.0.1:6379'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sitterfied',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': 'localhost',
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

# Override Facebook App ID
FACEBOOK_APP_ID = '746551758706532'

# Celery configuration
BROKER_URL = REDIS_URL + '/1'
CELERY_DEFAULT_QUEUE = 'sitterfied-dev'
CELERY_QUEUES = (
    Queue(CELERY_DEFAULT_QUEUE, Exchange(CELERY_DEFAULT_QUEUE, routing_key=CELERY_DEFAULT_QUEUE)),
)

# Celery Beat Configuration
CELERYBEAT_SCHEDULE = {
    'check-for-completed-jobs': {
        'task': 'sitterfied.app.tasks.jobs.check_for_completed_jobs',
        'schedule': crontab(minute='5'),
    },
    'check-for-canceled-jobs': {
        'task': 'sitterfied.app.tasks.jobs.check_for_canceled_jobs_with_incorrect_status',
        'schedule': crontab(hour='0', minute='15',),
    },
    'mark-expired-jobs': {
        'task': 'sitterfied.app.tasks.jobs.mark_expired_jobs',
        'schedule': crontab(minute='10'),
    },
}

# Override Job Reminder Times
FAST_SEND_REMINDERS = True
JOB_FIRST_REMINDER = 60
JOB_RELIEF_REMINDER = 180
JOB_SECOND_REMINDER = 120

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
