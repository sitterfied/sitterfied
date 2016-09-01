# -*- coding: utf-8 -*-
import logging
import re
import requests

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient
from twilio.twiml import Response

from sitterfied.app.utils import get_short_url
from sitterfied.bookings.models import AlreadyAcceptedException, Booking
from sitterfied.sitters.models import Sitter
from sitterfied.utils.models import IncomingSMSMessage

logger = logging.getLogger(__name__)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
sitterfied_number = settings.TWILIO_DEFAULT_CALLERID
client = TwilioRestClient(account_sid, auth_token)


response_pattern = '(accept|yes|decline|no)[^\d]*(\d+)'

@twilio_view
def sms_messages(request):
    from_number = request.POST.get('From', None)
    resp = Response()

    try:
        sitter = Sitter.objects.get(cell=from_number)
    except (Sitter.DoesNotExist, ObjectDoesNotExist):
        resp.sms('We\'re sorry, but this cell phone isn\'t registered.')
        return resp

    body = request.POST.get('Body')
    result = re.search(response_pattern, body, re.I | re.S)

    if result is None or len(result.groups()) < 2:
        resp.sms('We\'re sorry, but we couldn\'t understand your response. \
Please respond with either ACCEPT or DECLINE followed by the code you received.')
        return resp

    response = result.group(1).lower()
    request_id = result.group(2)

    try:
        booking = Booking.objects.get(id=request_id)
    except (Booking.DoesNotExist, ObjectDoesNotExist):
        resp.sms(
            'We\'re sorry, but we couldn\'t find job request ' + request_id + '. Please check the code and try again.')
        return resp

    if booking.canceled:
        resp.sms('We\'re sorry, but this job has been cancelled.')
        return resp

    if booking.declined_sitters.filter(pk=sitter.pk).exists():
        resp.sms('We\'re sorry, but you\'ve already declined this job.')
        return resp

    if not booking.sitters.filter(pk=sitter.pk).exists():
        resp.sms(
            'We\'re sorry, but we couldn\'t find job request ' + request_id + '. Please check the code and try again.')
        return resp

    if response in ['accept', 'yes', 'yeah', 'y', 'yup']:
        if booking.accepted_sitter == sitter:
            resp.sms(
                'Hi %s. Thanks for responding, but you\'ve already accepted this job.',
                (sitter.first_name),
            )
            return resp

        try:
            booking.accept(sitter)
        except AlreadyAcceptedException:
            resp.sms(
                'Hi %s. Thanks for responding, but this job has already been accepted.',
                (sitter.first_name),
            )
            return resp
    elif response in ['decline', 'no', 'nope', 'n']:
        if booking.accepted_sitter == sitter:
            short_url = get_short_url('/mybookings/upcoming')
            resp.sms('You have already ACCEPTED this job. If you\'d like to cancel, go here: ' + short_url)
        else:
            booking.decline(sitter)

    return resp


#for polling via cronjob
def get_new_messages():
    try:
        most_recent_message = IncomingSMSMessage.objects.all().order_by('-date_created')[0]
        most_recent = most_recent_message.date_created
        messages = client.sms.messages.list(to=sitterfied_number, after=most_recent)
    except IndexError:
        print "no messages yet"
        messages = client.sms.messages.list(to=sitterfied_number)
    for message in messages:
        new_message = IncomingSMSMessage(**message)
        new_message.save()


def send_message(body, to, is_parent=False):
    # Messages to parents are sent via the textit api so that all
    # messages originate from the same phone number. Messages to
    # sitters are sent directly via the twilio api.
    if is_parent:
        data = {
            'urns': ['tel:{}'.format(to)],
            'text': body,
        }
        requests.post(
            settings.TEXTIT_API_URL,
            data=data,
            headers={'Authorization': 'Token {}'.format(settings.TEXTIT_API_TOKEN)}
        )
    else:
        client.messages.create(body=body, to=to, from_=sitterfied_number)
