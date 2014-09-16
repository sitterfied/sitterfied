# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import braintree
import pytz
from celery.utils.log import get_task_logger
from django.db.models import Q

from app.models import Booking
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


def get_unsettled_jobs_since(timestamp):
    return Booking.objects.filter(
        stop_date_time__lte=timestamp
    ).filter(
        booking_status__iexact='completed'
    ).exclude(
        canceled=True
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


@app.task
def check_for_due_payments():
    """Check for any jobs that have payments due. Send out payments via
    Braintree.

    """
    jobs = get_unsettled_jobs_since(
        datetime.now(pytz.UTC) + timedelta(hours=1)
    )
    for job in jobs:
        hours = divmod((job.stop_date_time - job.start_date_time).seconds, 3600)[0]
        # TODO add promo code and sitterfied fee to the rate
        rate = job.rate * hours
        result = braintree.Transaction.sale({
            "payment_method_token": job.parent.default_payment_method_token,
            "amount": str(rate)
        })
        if result.is_success:
            job.booking_status = 'Paid'
            job.save()
        else:
            print result.message
    return jobs