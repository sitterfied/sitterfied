# -*- coding: utf-8 -*-
import logging

from sitterfied.bookings.models import Booking
from sitterfied.celeryapp import app
from sitterfied.utils import time
from sitterfied.utils.tasks import acquire_lock

logger = logging.getLogger(__name__)


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
    with acquire_lock('check-for-completed-since') as acquired:
        if acquired:
            return get_jobs_completed_since(time.now()).update(booking_status=Booking.BOOKING_STATUS_COMPLETED)


@app.task
def check_for_canceled_jobs_with_incorrect_status():
    """
    Check for any jobs that have been marked canceled, but where booking_status
    is not 'canceled'. Update status to 'canceled'.

    """
    with acquire_lock('check-for-canceled-jobs-with-incorrect-status') as acquired:
        if acquired:
            return get_canceled_jobs_with_incorrect_status().update(
                booking_status=Booking.BOOKING_STATUS_CANCELED
            )


@app.task
def mark_expired_jobs():
    """
    Mark any jobs that have expired since the last check as 'expired.'

    """
    with acquire_lock('mark-expired-jobs') as acquired:
        if acquired:
            jobs = get_jobs_expired_since(time.now())
            for job in jobs:
                job.responses \
                   .filter(response=Booking.BOOKING_STATUS_PENDING) \
                   .update(response=Booking.BOOKING_STATUS_EXPIRED, responded_at=time.now())

            return jobs.update(booking_status=Booking.BOOKING_STATUS_EXPIRED)
