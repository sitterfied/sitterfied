# -*- coding: utf-8 -*-
from datetime import datetime

import pytz
from celery.utils.log import get_task_logger
from django.db.models import Q

from sitterfied.bookings.models import Booking
from sitterfied.celeryapp import app


logger = get_task_logger(__name__)


def get_jobs_completed_since(timestamp):
    return Booking.objects.filter(
        stop_date_time__lte=timestamp
    ).filter(
        Q(booking_status__iexact='accepted') | Q(booking_status__iexact='pending')
    ).exclude(
        canceled=True
    )


def get_canceled_jobs_with_incorrect_status():
    return Booking.objects.filter(
        canceled=True
    ).exclude(
        booking_status__iexact='canceled'
    )


@app.task
def check_for_completed_jobs():
    """Check for any jobs that should have completed prior to the current
    time. Update the status of any jobs found to 'Completed'.

    """
    return get_jobs_completed_since(
        datetime.now(pytz.UTC)
    ).update(
        booking_status='Completed'
    )


@app.task
def check_for_canceled_jobs_with_incorrect_status():
    """Check for any jobs that have been marked canceled, but where booking_status
    is not 'Canceled'. Update status to 'Canceled'.

    """
    return get_canceled_jobs_with_incorrect_status().update(
        booking_status='Canceled'
    )
