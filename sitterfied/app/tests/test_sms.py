# -*- coding: utf-8 -*-
import app.sms as sms
import mock
import xml.etree.ElementTree as ET

from app.models import Booking, Sitter
from django.conf import settings
from django.test.client import RequestFactory
from hamcrest import *
from twilio.rest import TwilioRestClient

TWILIO_TEST_CALLERID = '+15005550006'

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
default_callerid = '+19088384816'
from_number = '+12035175070'

client = TwilioRestClient(account_sid, auth_token)

test_client = TwilioRestClient('ACa61e8d05687a561ad45eaaa73c1e1b30', 'bb1f89140947daea0bbc62335b8b92ec')

request_factory = RequestFactory()


class SitterManager():
    """Mock class for simulating a ManyToManyRelatedManager"""
    def __init__(self, sitter):
        self.sitter = sitter

    def all(self):
        return [self.sitter]

    def get(self, **kwargs):
        return self.sitter


def test_send_sms_message():
    message_id = test_client.sms.messages.create(body='Test', to='+17322397588', from_=TWILIO_TEST_CALLERID)
    assert_that(message_id, not_none())


def test_sms_messages_no_cell():
    request = request_factory.post('sms/', {'From': from_number,
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
    request = request_factory.post('sms/', {'From': from_number,
                                            'To': default_callerid,
                                            'Body': 'jfdkfsdfsd'})

    with mock.patch('app.sms.Sitter') as mock_sitter:
        mock_sitter.objects = SitterManager(mock_sitter)

        response = sms.sms_messages(request)
        assert_that(response, not_none())
        assert_that(response.content, not_none())

        xml = ET.fromstring(response.content)
        message = xml.find('Sms')
        assert_that(message.text, is_('We\'re sorry, but we couldn\'t understand \
your response. Please respond with either ACCEPT or DECLINE \
followed by the code you received.'))


def test_sms_messages_booking_does_not_exist():
    request = request_factory.post('sms/', {'From': from_number,
                                            'To': default_callerid,
                                            'Body': 'Accept 0'})

    with mock.patch('app.sms.Booking') as mock_booking:
        with mock.patch('app.sms.Sitter') as mock_sitter:
            mock_sitter.objects = SitterManager(mock_sitter)
            mock_booking.objects.get.side_effect = Booking.DoesNotExist

            response = sms.sms_messages(request)
            assert_that(response, not_none())
            assert_that(response.content, not_none())

            xml = ET.fromstring(response.content)
            message = xml.find('Sms')
            assert_that(message.text, is_('We\'re sorry, but we couldn\'t find job request 0. Please check the code and try again.'))


def test_sms_messages_booking_already_accepted():
    request = request_factory.post('sms/', {'From': from_number,
                                            'To': default_callerid,
                                            'Body': 'Accept 0'})

    with mock.patch('app.sms.Booking') as mock_booking:
        with mock.patch('app.sms.Sitter') as mock_sitter:
            mock_booking.objects.get.return_value = return_value = mock.Mock()
            mock_sitter.objects.get.return_value = sitter = mock.Mock()

            sitter.first_name = 'Devon'
            return_value.sitters = SitterManager(sitter)

            response = sms.sms_messages(request)
            assert_that(response, not_none())
            assert_that(response.content, not_none())

            xml = ET.fromstring(response.content)
            message = xml.find('Sms')
            assert_that(message.text, is_('Hi Devon. Thanks for responding, but this job has already been accepted.'))


def test_sms_messages_success():
    request = request_factory.post('sms/', {'From': from_number,
                                            'To': default_callerid,
                                            'Body': 'Accept 0'})

    with mock.patch('app.sms.Booking') as mock_booking:
        with mock.patch('app.sms.Sitter') as mock_sitter:
            mock_sitter.objects.get.return_value = sitter = mock.Mock()

            mock_booking.objects.get.return_value = return_value = mock.Mock()
            return_value.accepted_sitter = None
            return_value.sitters = SitterManager(sitter)

            response = sms.sms_messages(request)
            assert_that(response, not_none())
            assert_that(response.content, not_none())

            xml = ET.fromstring(response.content)
            message = xml.find('Sms')
            assert_that(message, none())
