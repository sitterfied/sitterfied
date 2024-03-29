# -*- coding: utf-8 -*-
import logging
import re

from delorean import Delorean
from django.template.loader import render_to_string
from django.utils import timezone
from twilio import TwilioRestException

from sitterfied.app.sms import send_message
from sitterfied.app.utils import get_short_url
from sitterfied.bookings.models import Booking, BookingResponse
from sitterfied.celeryapp import app

logger = logging.getLogger(__name__)
ansi_escape = re.compile(r'\x1b[^m]*m')


@app.task
def notify_parent_of_job_request(id):
    try:
        booking = Booking.objects.get(pk=id)
    except Booking.DoesNotExist:
        return

    parent = booking.parent

    if parent.settings.mobile_booking_accepted_denied:
        if booking.booking_type in ['meetup', 'phone']:
            sms_template = 'sms/interview/interview_request_parent_confirmation.sms'
        else:
            sms_template = 'sms/booking/booking_request_sent.sms'

        try:
            sms = render_to_string(sms_template, {'short_url': get_short_url('/mybookings/pending')})
            send_message(body=sms, to=parent.cell, is_parent=True)
        except Exception as ex:
            logger.error(
                'Notification to %s with cell number %s failed for the following reason: %s',
                parent.get_full_name(),
                parent.cell,
                ansi_escape.sub('', ex.msg),
            )


@app.task
def notify_sitter_of_job_request(id):
    try:
        booking_response = BookingResponse.objects.get(pk=id)
    except BookingResponse.DoesNotExist:
        return

    booking = booking_response.booking
    sitter = booking_response.sitter
    parent = booking.parent
    multi_request_suffix = '_multiple' if booking.sitters.count() > 1 else ''

    if sitter.settings.mobile_booking_request and sitter.cell:
        if booking.booking_type in ['meetup', 'phone']:
            booking_type = '{}_interview'.format(booking.booking_type)
            sms_template = 'sms/interview/{0}_request_to_sitter.sms'.format(booking_type)
        else:
            sms_template = 'sms/booking/booking_request_received{0}.sms'.format(multi_request_suffix)

        start_date_time = Delorean(booking.start_date_time).shift(booking.time_zone).datetime
        stop_date_time = Delorean(booking.stop_date_time).shift(booking.time_zone).datetime
        booking_date = start_date_time.date()

        try:
            # Django templates will shift the time based on the
            # time zone so we need to activate the time zone of the
            # job.
            timezone.activate(booking.time_zone)

            sms = render_to_string(sms_template, {
                'sitter_name': sitter.first_name,
                'parent_name': parent.get_full_name(),
                'booking_date': booking_date,
                'start_date_time': start_date_time,
                'stop_date_time': stop_date_time,
                'parent_city': parent.city,
                'short_url': get_short_url('/mybookings/pending'),
                'booking_code': booking.id,
                'num_sitters': booking.sitters.count() - 1,
            })
            send_message(body=sms, to=sitter.cell)
        except TwilioRestException as ex:
            logger.error(
                'Notification to %s with cell number %s failed for the following reason: %s',
                sitter.get_full_name(),
                sitter.cell,
                ansi_escape.sub('', ex.msg),
            )
        finally:
            timezone.deactivate()
