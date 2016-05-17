# -*- coding: utf-8 -*-
import mock
import re
import xml.etree.ElementTree as ET

from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory
from hamcrest import assert_that, is_, none, not_none
from twilio.rest import TwilioRestClient
from unittest import skip

from sitterfied.app import sms
from sitterfied.bookings.models import Booking


TWILIO_TEST_CALLERID = '+15005550006'

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
default_callerid = '+19088384816'
from_number = '+12035175070'

client = TwilioRestClient(account_sid, auth_token)

test_client = TwilioRestClient('ACa61e8d05687a561ad45eaaa73c1e1b30', 'bb1f89140947daea0bbc62335b8b92ec')

request_factory = RequestFactory()


class SitterManager():
    """
    Mock class for simulating a ManyToManyRelatedManager

    """
    def __init__(self, sitter):
        self.sitter = sitter

    def all(self):
        return [self.sitter]

    def get(self, **kwargs):
        return self.sitter


@skip
class SmsTestCase(TestCase):

    def test_send_sms_message(self):
        message_id = test_client.sms.messages.create(body='Test', to='+17322397588', from_=TWILIO_TEST_CALLERID)
        assert_that(message_id, not_none())

    def test_sms_messages_no_cell(self):
        request = request_factory.post('sms/', {
            'From': from_number,
            'To': default_callerid,
            'Body': 'Accept 0'
        })

        with mock.patch('sitterfied.app.sms.Sitter') as mock_model:
            from sitterfied.app.models import Sitter

            mock_model.objects.get.side_effect = Sitter.DoesNotExist

            response = sms.sms_messages(request)
            assert_that(response, not_none())
            assert_that(response.content, not_none())

            xml = ET.fromstring(response.content)
            message = xml.find('Sms')
            assert_that(message.text, is_('We\'re sorry, but this cell phone isn\'t registered.'))

    def test_sms_messages_response_not_understood(self):
        request = request_factory.post('sms/', {
            'From': from_number,
            'To': default_callerid,
            'Body': 'jfdkfsdfsd'
        })

        with mock.patch('sitterfied.app.sms.Sitter') as mock_sitter:
            mock_sitter.objects = SitterManager(mock_sitter)

            response = sms.sms_messages(request)
            assert_that(response, not_none())
            assert_that(response.content, not_none())

            xml = ET.fromstring(response.content)
            message = xml.find('Sms')
            assert_that(message.text, is_(
                'We\'re sorry, but we couldn\'t understand \
                your response. Please respond with either ACCEPT or DECLINE \
                followed by the code you received.'
            ))

    def test_sms_messages_booking_does_not_exist(self):
        request = request_factory.post('sms/', {
            'From': from_number,
            'To': default_callerid,
            'Body': 'Accept 0'
        })

        with mock.patch('sitterfied.app.sms.Booking') as mock_booking:
            with mock.patch('sitterfied.app.sms.Sitter') as mock_sitter:
                mock_sitter.objects = SitterManager(mock_sitter)
                mock_booking.objects.get.side_effect = Booking.DoesNotExist

                response = sms.sms_messages(request)
                assert_that(response, not_none())
                assert_that(response.content, not_none())

                xml = ET.fromstring(response.content)
                message = xml.find('Sms')
                assert_that(message.text, is_(
                    'We\'re sorry, but we couldn\'t find job request 0. Please check the code and try again.'
                ))

    def test_sms_messages_booking_already_accepted(self):
        request = request_factory.post('sms/', {
            'From': from_number,
            'To': default_callerid,
            'Body': 'Accept 0'
        })

        with mock.patch('sitterfied.app.sms.Booking') as mock_booking:
            with mock.patch('sitterfied.app.sms.Sitter') as mock_sitter:
                mock_booking.objects.get.return_value = return_value = mock.Mock()
                mock_sitter.objects.get.return_value = sitter = mock.Mock()

                sitter.first_name = 'Devon'
                return_value.sitters = SitterManager(sitter)

                response = sms.sms_messages(request)
                assert_that(response, not_none())
                assert_that(response.content, not_none())
                xml = ET.fromstring(response.content)
                message = xml.find('Sms')
                assert_that(message.text, is_(
                    'Hi Devon. Thanks for responding, but this job has already been accepted.'
                ))

    def test_sms_messages_success(self):
        request = request_factory.post('sms/', {
            'From': from_number,
            'To': default_callerid,
            'Body': 'Accept 0'
        })

        with mock.patch('sitterfied.app.sms.Booking') as mock_booking:
            with mock.patch('sitterfied.app.sms.Sitter') as mock_sitter:
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

    def test_regex_response_pattern(self):
        pattern = sms.response_pattern

        result = re.search(pattern, 'DEcline 187', re.I | re.S)
        assert_that(result, not_none())
        assert_that(len(result.groups()), is_(2))
        assert_that(result.group(1).lower(), is_('decline'))
        assert_that(result.group(2), is_('187'))

        result = re.search(pattern, 'accePT 343', re.I | re.S)
        assert_that(result, not_none())
        assert_that(len(result.groups()), is_(2))
        assert_that(result.group(1).lower(), is_('accept'))
        assert_that(result.group(2), is_('343'))

        assert_that(re.search(pattern, 'decCline   ', re.I | re.S), none())
        assert_that(re.search(pattern, 'dsgdfgfdgfd', re.I | re.S), none())
        assert_that(re.search(pattern, 'dsfdsw243242', re.I | re.S), none())
        assert_that(re.search(pattern, '  accept', re.I | re.S), none())
