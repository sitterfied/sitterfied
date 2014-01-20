# -*- coding: utf-8 -*-
import app.sms as sms
import mock
import xml.etree.ElementTree as ET

from django.conf import settings
from django.test.client import RequestFactory
from hamcrest import *
from twilio.rest import TwilioRestClient

TWILIO_TEST_CALLERID = '+15005550006'

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
default_callerid = '+19088384816'

client = TwilioRestClient(account_sid, auth_token)

test_client = TwilioRestClient('ACa61e8d05687a561ad45eaaa73c1e1b30', 'bb1f89140947daea0bbc62335b8b92ec')

request_factory = RequestFactory()

def test_send_sms_message():
    message_id = test_client.sms.messages.create(body='Test', to='+17322397588', from_=TWILIO_TEST_CALLERID)
    assert_that(message_id, not_none())

def test_sms_messages_no_cell():
    request = request_factory.post('sms/', {'From': '+15555555555',
                                            'To': default_callerid,
                                            'Body': 'Accept 0'})

    with mock.patch('app.sms.Sitter') as mock_model:
        from app.models import Sitter

        mock_model.objects.get.side_effect = Sitter.DoesNotExist

        response = sms.sms_messages(request)
        assert_that(response, not_none())
        assert_that(response.content, not_none())

        xml = ET.fromstring(response.content)
        message = xml.find('Sms')
        assert_that(message.text, is_('We\'re sorry, but this cell phone isn\'t registered.'))

def test_sms_messages_response_not_understood():
    request = request_factory.post('sms/', {'From': '+17322397588',
                                            'To': default_callerid,
                                            'Body': 'jfdkfsdfsd'})

    response = sms.sms_messages(request)
    assert_that(response, not_none())
    assert_that(response.content, not_none())

    xml = ET.fromstring(response.content)
    message = xml.find('Sms')
    assert_that(message.text, is_('We\'re sorry, but we couldn\'t understand \
your response. Please respond with either the word \'Accept\' or \'Decline\' \
followed by the code you received.'))

def test_sms_messages_booking_does_not_exist():
    request = request_factory.post('sms/', {'From': '+17322397588',
                                            'To': default_callerid,
                                            'Body': 'Accept 0'})

    with mock.patch('app.sms.Booking') as mock_booking:
        from app.models import Booking

        mock_booking.objects.get.side_effect = Booking.DoesNotExist

        response = sms.sms_messages(request)
        assert_that(response, not_none())
        assert_that(response.content, not_none())

        xml = ET.fromstring(response.content)
        message = xml.find('Sms')
        assert_that(message.text, is_('We\'re sorry, but we couldn\'t find a booking request that matches the code you sent.'))

def test_sms_messages_booking_already_accepted():
    request = request_factory.post('sms/', {'From': '+17322397588',
                                            'To': default_callerid,
                                            'Body': 'Accept 0'})

    with mock.patch('app.sms.Booking') as mock_booking:
        mock_booking.objects.get = mock.Mock()

        response = sms.sms_messages(request)
        assert_that(response, not_none())
        assert_that(response.content, not_none())

        xml = ET.fromstring(response.content)
        message = xml.find('Sms')
        assert_that(message.text, is_('We\'re sorry, but this booking has already been accepted.'))

def test_sms_messages_success():
    request = request_factory.post('sms/', {'From': '+17322397588',
                                            'To': default_callerid,
                                            'Body': 'Accept 0'})

    with mock.patch('app.sms.Booking') as mock_booking:
        mock_booking.objects.get.return_value = return_value = mock.Mock()
        return_value.accepted_sitter = None

        response = sms.sms_messages(request)
        assert_that(response, not_none())
        assert_that(response.content, not_none())

        xml = ET.fromstring(response.content)
        message = xml.find('Sms')
        assert_that(message, none())
