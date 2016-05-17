# -*- coding: utf-8 -*-
import autofixture

from datetime import datetime, timedelta
from django.db.models.signals import post_save, pre_delete
from django.template.loader import render_to_string
from hamcrest import assert_that, is_
from mock import patch

from sitterfied.app import signals
from sitterfied.app.tasks import reminders
from sitterfied.app.tasks.tests import utils
from sitterfied.bookings.models import Booking, Reminder
from sitterfied.test.testcases import SitterfiedApiTestCase


class TestReminders(SitterfiedApiTestCase):

    def setUp(self):
        disconnect_signals()

    def teardown(self):
        reconnect_signals()

    def test_get_time_delta(self):
        # Hours
        assert_that(reminders.get_time_delta(1 * 3600), is_('in 1 hour'))
        assert_that(reminders.get_time_delta(18 * 3600), is_('in 18 hours'))
        assert_that(reminders.get_time_delta(24 * 3600), is_('tomorrow'))
        assert_that(reminders.get_time_delta(36 * 3600), is_('tomorrow'))
        assert_that(reminders.get_time_delta(48 * 3600), is_('in 2 days'))
        assert_that(reminders.get_time_delta(52 * 3600), is_('in 2 days'))
        assert_that(reminders.get_time_delta(72 * 3600), is_('in 3 days'))

        # Minutes
        assert_that(reminders.get_time_delta(24 * 60), is_('in 24 minutes'))
        assert_that(reminders.get_time_delta(1 * 60), is_('in 1 minute'))

    def test_first_reminder_strings(self):
        now = datetime.utcnow()
        stop_time = now + timedelta(hours=1)
        cell = '+15555555555'
        first_name = 'Jane'
        name = 'Jane Doe'
        delta = reminders.get_time_delta(3600)
        sms = render_to_string('sms/reminder/parent/first_reminder.sms', {
            'sitter_full_name': name,
            'sitter_first_name': first_name,
            'sitter_cell': cell,
            'timedelta': delta,
            'start_date_time': now,
            'stop_date_time': stop_time,
            'short_url': '/mybookings/upcoming',
        })

        assert_that(sms, is_(u'{0} will be arriving {1}. {2}\'s # is: {3}. Go to {4} for details.\n'.format(
            name,
            delta,
            first_name,
            cell,
            '/mybookings/upcoming',
        )))

    def test_relief_reminder_strings(self):
        now = datetime.utcnow()
        cell = '+15555555555'
        name = 'Jane'
        delta = reminders.get_time_delta(3600)
        sms = render_to_string('sms/reminder/parent/relieve_sitter_reminder.sms', {
            'sitter_first_name': name,
            'sitter_cell': cell,
            'timedelta': delta,
            'stop_date_time': now,
        })

        assert_that(sms, is_(u'Friendly reminder that you need to relieve {0} {3} ({2}). {0}\u2019s # is: {1}. Try not to be late :)\n'.format(
            name,
            cell,
            get_time_code(now),
            delta,
        )))

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.signals.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.signals.notifications.notify_parent_of_job_request.delay')
    @patch('sitterfied.app.tasks.reminders.send_message')
    def test_send_reminders(self, send_message, notify_parent, notify_sitter, get_time_zone):
        booking = None
        reminder = None
        response = None

        try:
            booking = autofixture.get('app.Booking').create_one()

            response = booking.responses.first()
            response.response = Booking.BOOKING_STATUS_ACCEPTED
            response.responded_at = datetime.now()
            response.save()

            reminder = Reminder()
            reminder.booking = booking
            reminder.save()

            reminders.send_reminders(reminder.id, 'first', 1, [])
            assert_that(send_message.call_count, is_(2))

            reminders.send_reminders(reminder.id, 'second', 2, [])
            assert_that(send_message.call_count, is_(4))
        finally:
            booking.delete()
            response.delete()
            reminder.delete()


def get_time_code(instant):
    hour = instant.strftime('%I').lstrip('0')
    rest = instant.strftime(':%M%p').lower()
    return hour + rest


def disconnect_signals():
    utils.disconnect_signal(post_save, signals.reminder_save_handler, Reminder)
    utils.disconnect_signal(pre_delete, signals.reminder_del_handler, Reminder)


def reconnect_signals():
    utils.reconnect_signal(post_save, signals.reminder_save_handler, Reminder)
    utils.reconnect_signal(pre_delete, signals.reminder_del_handler, Reminder)
