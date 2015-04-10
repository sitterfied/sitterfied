# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from delorean.dates import utc
from hamcrest import all_of, assert_that, contains_string, is_
from mock import patch

from sitterfied.app.tasks import notifications
from sitterfied.bookings.models import Booking, BookingResponse
from sitterfied.parents.models import Parent
from sitterfied.utils.test import SitterfiedApiTestCase, create_sitters


def convert_time_string(time):
    return time.strftime('%I:%M%p').lower().lstrip('0')


class TestNotifications(SitterfiedApiTestCase):

    def setUp(self):
        super(TestNotifications, self).setUp()

        parent = Parent.objects.create(
            first_name='Parent',
            last_name='One',
            cell='+15555555555',
            email='parent.one@gmail.com',
            timezone='America/New_York',
        )
        sitter = create_sitters(1)[0]
        self.start_date_time = datetime.now(utc)
        self.stop_date_time = self.start_date_time + timedelta(hours=4)
        with patch('sitterfied.app.tasks.notifications.send_message') as send_message:
            self.booking = Booking.objects.create(
                address1='501 Adams St',
                address2='Apt 3K',
                city='Hoboken',
                num_children=1,
                parent=parent,
                start_date_time=self.start_date_time,
                state='NJ',
                stop_date_time=self.stop_date_time,
                zip='07030',
            )
            self.response = BookingResponse.objects.create(sitter=sitter, booking=self.booking)
            assert_that(send_message.call_count, is_(2))

    @patch('sitterfied.app.tasks.notifications.send_message')
    def test_notify_parent_of_job_request(self, send_message):
        notifications.notify_parent_of_job_request(self.booking.id)
        assert_that(send_message.call_count, is_(1))
        assert_that(send_message.call_args[1].get('body'), contains_string('Job request sent!'))

    @patch('sitterfied.app.tasks.notifications.send_message')
    def test_notify_sitter_of_job_request(self, send_message):
        notifications.notify_sitter_of_job_request(self.response.id)
        assert_that(send_message.call_count, is_(1))
        start_time = convert_time_string(self.start_date_time)
        stop_time = convert_time_string(self.stop_date_time)
        assert_that(send_message.call_args[1].get('body'),
            all_of(contains_string('{0}-{1}'.format(start_time, stop_time)), contains_string('ACCEPT 1 or DECLINE 1'))
        )
