# -*- coding: utf-8 -*-
from datetime import datetime

import pytz
from celery.utils.log import get_task_logger

from sitterfied.bookings.models import Booking
from sitterfied.celeryapp import app


logger = get_task_logger(__name__)


def get_jobs_completed_since(timestamp):
    return Booking.objects.filter(
        stop_date_time__lte=timestamp
    ).filter(
        booking_status__iexact=Booking.BOOKING_STATUS_ACCEPTED
    ).exclude(
        canceled=True
    )


def get_jobs_expired_since(timestamp):
    return Booking.objects.filter(
        stop_date_time__lte=timestamp
    ).filter(
        booking_status__iexact=Booking.BOOKING_STATUS_PENDING
    ).exclude(
        canceled=True
    )


def get_canceled_jobs_with_incorrect_status():
    return Booking.objects.filter(
        canceled=True
    ).exclude(
        booking_status__iexact=Booking.BOOKING_STATUS_CANCELED
    )


@app.task
def check_for_completed_jobs():
    """
    Check for any jobs that should have completed prior to the current
    time. Update the status of any jobs found to 'completed'.

    """
    return get_jobs_completed_since(
        datetime.now(pytz.UTC)
    ).update(
        booking_status=Booking.BOOKING_STATUS_COMPLETED
    )


@app.task
def check_for_canceled_jobs_with_incorrect_status():
    """
    Check for any jobs that have been marked canceled, but where booking_status
    is not 'canceled'. Update status to 'canceled'.

    """
    return get_canceled_jobs_with_incorrect_status().update(
        booking_status=Booking.BOOKING_STATUS_CANCELED
    )


@app.task
def mark_expired_jobs():
    """
    Mark any jobs that have expired since the last check as 'expired.'

    """
    return get_jobs_expired_since(datetime.now(pytz.UTC)).update(
        booking_status=Booking.BOOKING_STATUS_EXPIRED
    )
