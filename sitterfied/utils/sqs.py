# -*- coding: utf-8 -*-
import logging
import re

from boto import ec2
from boto import sqs
from boto.exception import SQSError
from django.conf import settings

logger = logging.getLogger(__name__)
queue_ip_re = re.compile(r'ip-(?P<ip>\d+-\d+-\d+-\d+)')


def get_running_ips(region='us-east-1'):
    """
    Retrieve an array of private IP's for all running instances in a region.

    """
    ips = []
    conn = ec2.connect_to_region(
        region,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    reservations = conn.get_all_instances()
    for reservation in reservations:
        for instance in reservation.instances:
            ips.append(instance.private_ip_address)
    return ips


def get_all_queues(region='us-east-1'):
    """
    Retrieve all the sqs queues within a region

    """
    conn = sqs.connect_to_region(
        region,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    return conn.get_all_queues()


def queue_name_to_ip(queue_name):
    """
    Convert a queue name to an ip address or None

    Celery queue names in sqs look like:
    "worker0_ip-172-31-16-150-celery-pidbox"
    Which we need to convert to 172.31.16.150 to then match against.
    """
    try:
        return queue_ip_re.search(queue_name).group('ip').replace('-', '.')
    except (IndexError, AttributeError):
        return None


def get_stale_queues(region='us-east-1'):
    """
    Retrieve a list of queues that we deem stale

    A stale queue is one who's instance is no longer running. We can determine
    this by the queue name which contains the private ip of the instance that
    spawned it.
    """
    running_ips = get_running_ips(region)
    stale_queues = []
    for queue in get_all_queues(region):
        ip = queue_name_to_ip(queue.name)
        if ip and not ip in running_ips:
            stale_queues.append(queue)
    return stale_queues


def cleanup_stale_queues(region='us-east-1', dry_run=False):
    """
    Retrieve and clean up any stale queues

    Stale queues will be identified and queried for available messages before
    being removed.
    """
    stale_queues = get_stale_queues()
    for queue in stale_queues:
        try:
            queue_len = len(queue.get_messages())
        except SQSError:
            continue
        if queue_len == 0:
            logger.info("Found stale queue {}{}".format(
                queue.name, '' if dry_run else ', removing it'))
            if not dry_run:
                queue.delete()
