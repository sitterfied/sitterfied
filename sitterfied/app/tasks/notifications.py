# -*- coding: utf-8 -*-
import logging
import pytz

from django.template.loader import render_to_string
from django.utils import timezone
from twilio import TwilioRestException

from sitterfied.app.sms import send_message
from sitterfied.app.utils import get_short_url
from sitterfied.bookings.models import Booking, BookingResponse
from sitterfied.celeryapp import app
from sitterfied.utils import time

logger = logging.getLogger(__name__)


@app.task
def notify_parent_of_job_request(id):
    try:
        booking = Booking.objects.get(pk=id)
    except Booking.DoesNotExist:
        pass

    if booking:
        parent = booking.parent

        if parent.settings.email_booking_accepted_denied:
            pass  # TODO: implement email for parent request sent

        if parent.settings.mobile_booking_accepted_denied:
            if booking.booking_type in ['meetup', 'phone']:
                sms_template = 'sms/interview/interview_request_parent_confirmation.sms'
            else:
                sms_template = 'sms/booking/booking_request_sent.sms'
            try:
                sms = render_to_string(sms_template, {'short_url': get_short_url('/mybookings/pending')})
                send_message(body=sms, to=parent.cell)
            except:
                pass


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

    if sitter.settings.email_booking_request:
        """
        *|FULL_NAME|* [URL link to parent's profile page] would like you to
        sit for *|CHILD_1|*, *|CHILD_2|* and *|CHILD_3|* on *|JOB_DATE|* from
        *|FROM_TIME|* to *|TO_TIME|*.

        The job is located at *|JOB_ADDRESS|*

        Go to your bookings page [URL link to sitter's bookings page] to
        Accept or Decline this job.

        *|FNAME|* added a note- "*|SHOW_NOTE|*"

        You can reach *|FNAME|* by email: *|EMAIL|* or phone: *|MOBILE|*
        """
        # message = create_message_base()
        # message['subject'] = 'You have a new job request!'
        # message['to'] = [create_email_to(sitter.email, sitter.get_full_name())]
        # message['global_merge_vars'] = [{
        #     'FNAME': sitter.first_name,
        #     'PARENT_NAME': parent.get_full_name(),
        #     'PARENT_URL': '/profile/' + str(parent.id),
        # }]
        # TODO: send_template_email('', message)

    if sitter.settings.mobile_booking_request and sitter.cell:
        if booking.booking_type in ['meetup', 'phone']:
            booking_type = '{}_interview'.format(booking.booking_type)
            sms_template = 'sms/interview/{0}_request_to_sitter.sms'.format(booking_type)
        else:
            sms_template = 'sms/booking/booking_request_received{0}.sms'.format(multi_request_suffix)

        booking_date = booking.start_date_time.date()
        tz = time.get_timezone(sitter.timezone)
        start_date_time = tz.normalize(booking.start_date_time)
        stop_date_time = tz.normalize(booking.stop_date_time)

        try:
            # Activate the timezone for the sitter so that dates
            # are formatted correctly.
            timezone.activate(sitter.timezone if sitter.timezone else pytz.UTC)
            sms = render_to_string(sms_template, {
                'sitter_name': sitter.first_name,
                'parent_name': parent.get_full_name(),
                'booking_date': booking_date,
                'start_date_time': start_date_time.replace(),
                'stop_date_time': stop_date_time.replace(),
                'parent_city': parent.city,
                'short_url': get_short_url('/mybookings/pending'),
                'booking_code': booking.id,
                'num_sitters': len(booking.sitters.all()) - 1,
            })
            send_message(body=sms, to=sitter.cell)
        except TwilioRestException as ex:
            logger.error(
                'Notification to {0} with cell number {1} failed for the following reason: {2}',
                sitter.get_full_name(),
                sitter.cell,
                str(ex),
            )
        finally:
            timezone.deactivate()
