# -*- coding: utf-8 -*-
import random

from delorean import Delorean
from hamcrest import all_of, assert_that, contains_string, is_
from mock import patch

from sitterfied.app.tasks import notifications
from sitterfied.utils.test import SitterfiedApiTestCase
from sitterfied.utils.tests.autofixtures import create_bookings

time_zone = 'America/New_York'


def convert_time_string(time):
    return time.strftime('%I:%M%p').lower().lstrip('0')


class TestNotifications(SitterfiedApiTestCase):

    def setUp(self):
        super(TestNotifications, self).setUp()

        self.booking = create_bookings()

    @patch('sitterfied.app.tasks.notifications.send_message')
    def test_notify_parent_of_job_request(self, send_message):
        notifications.notify_parent_of_job_request(self.booking.id)
        assert_that(send_message.call_count, is_(1))
        assert_that(send_message.call_args[1].get('body'), contains_string('Job request sent!'))

    @patch('sitterfied.app.tasks.notifications.send_message')
    def test_notify_sitter_of_job_request(self, send_message):
        response = random.choice(self.booking.responses.all())
        notifications.notify_sitter_of_job_request(response.id)
        assert_that(send_message.call_count, is_(1))
        start_time = convert_time_string(
            Delorean(
                datetime=self.booking.start_date_time,
                timezone='UTC').shift(time_zone).datetime
        )
        stop_time = convert_time_string(
            Delorean(
                datetime=self.booking.stop_date_time,
                timezone='UTC').shift(time_zone).datetime
        )
        assert_that(send_message.call_args[1].get('body'),
            all_of(contains_string('{0}-{1}'.format(start_time, stop_time)), contains_string('ACCEPT 1 or DECLINE 1'))
        )
