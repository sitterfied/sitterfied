# -*- coding: utf-8 -*-
from .base import *
from .mandrill import *

from celery.schedules import crontab
from urllib import quote_plus

DEBUG = False

# AWS Settings
AWS_REGION = 'us-east-1'
AWS_ACCESS_KEY_ID = 'AKIAIRC5KBNUD4ERCW5A'
AWS_SECRET_ACCESS_KEY = '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'

# Send Admin emails from the test subdomain
SERVER_EMAIL = 'no-reply@test.sitterfied.com'

MIDDLEWARE_CLASSES += (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

# Celery Configuration
BROKER_TRANSPORT_OPTIONS = {
    'region': AWS_REGION,
    # Set visibility timeout to 1 year, this is necessary to prevent
    # celery from executing scheduled celery tasks multiple times.
    'visibility_timeout': 43200,

}

BROKER_URL = 'sqs://{}:{}@'.format(AWS_ACCESS_KEY_ID, quote_plus(AWS_SECRET_ACCESS_KEY))

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
    'cleanup-stale-sqs-queues': {
        'task': 'sitterfied.utils.tasks.cleanup_stale_sqs_queues',
        'schedule': crontab(hour='*', minute=0, day_of_week='*'),
    },
    'update-knowtify': {
        'task': 'sitterfied.utils.knowtify.update_knowtify',
        'schedule': crontab(hour=22, minute=3, day_of_week='Mon'),
    },
}
