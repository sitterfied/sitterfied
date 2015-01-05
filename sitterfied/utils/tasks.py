# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.core.cache import cache

from sitterfied.celeryapp import app
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


@app.task
def cleanup_stale_sqs_queues(region='us-east-1'):
    """
    Task wrapper around the sqs cleanup function.

    """
    with acquire_lock('cleanup-stale-sqs-queues') as acquired:
        if acquired:
            logger.info("Cleaning up stale sqs queues")
            cleanup_stale_queues(region)
