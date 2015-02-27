# -*- coding: utf-8 -*-
import logging
import pytz

from celery import signature
from datetime import datetime, timedelta
from django.conf import settings
from django.core.cache import cache
from functools import wraps

from sitterfied.celeryapp import app
from sitterfied.utils import time
from sitterfied.utils.sqs import cleanup_stale_queues

logger = logging.getLogger(__name__)


class acquire_lock(object):
    """
    Context manager that attempts to acquire a lock for the given lock_key and
    then releases the lock afterwards.

    """
    def __init__(self, lock_key, expires=settings.DEFAULT_TASK_LOCK_EXPIRE):
        self.lock_key = lock_key
        self.expires = expires

    def __enter__(self):
        return cache.add(self.lock_key, 'true', self.expires)

    def __exit__(self, exc_type, exc_value, traceback):
        return cache.delete(self.lock_key)


def get_eta(desired_eta):
    visibility_timeout = settings.BROKER_TRANSPORT_OPTIONS.get('visibility_timeout')
    return min(desired_eta, time.now() + timedelta(seconds=visibility_timeout))


def reschedule(delta=None):
    delta = delta or timedelta(minutes=5)

    def reschedule_decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            desired_eta = kwargs.get('desired_eta', None)
            if not desired_eta:
                logger.info('No desired eta specified, executing task.')
                func(*args, **kwargs)
                return

            eta = desired_eta
            if isinstance(eta, (unicode, str)):
                eta = time.make_aware(datetime.strptime(eta, '%Y-%m-%d %H:%M:%S'), pytz.UTC)
            now = time.now()
            if now - delta < eta < now + delta:
                logger.info('Desired eta falls within time window, executing task.')
                func(*args, **kwargs)
                return
            elif eta > now:
                logger.info('Desired eta has passed, executing task.')
                func(*args, **kwargs)
                return

            eta = get_eta(eta)
            logger.info(
                'Desired eta ({}) not yet reached, rescheduling task for {}.'
                .format(desired_eta, eta.strftime('%Y-%m-%d %H:%M:%S')))
            task_name = '{}.{}'.format(func.func_globals.get('__name__'), func.func_name)
            signature(task_name).apply_async(eta=eta, kwargs=kwargs)
        return func_wrapper
    return reschedule_decorator


@app.task
def cleanup_stale_sqs_queues(region='us-east-1'):
    """
    Task wrapper around the sqs cleanup function.

    """
    with acquire_lock('cleanup-stale-sqs-queues') as acquired:
        if acquired:
            logger.info("Cleaning up stale sqs queues")
            cleanup_stale_queues(region)
