# -*- coding: utf-8 -*-
import autofixture

from datetime import datetime, timedelta
from hamcrest import assert_that, contains, is_
from mock import patch
from rest_framework import reverse, status

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.utils.test import SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    expected_properties = BookingSerializer.Meta.fields

    def setUp(self):
        super(TestViews, self).setUp()

        self.parent = autofixture.get('app.Parent').create_one()
        self.data = {
            'address1': '501 Adams St',
            'address2': 'Apt 2E',
            'city': 'Hoboken',
            'num_children': 1,
            'parent': self.parent.id,
            'start_date_time': datetime.now(),
            'state': 'NJ',
            'sitters': [sitter.id for sitter in self.parent.sitter_teams.all()],
            'stop_date_time': datetime.now() + timedelta(hours=4),
            'zip': '07030',
        }

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.signals.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.signals.notifications.notify_parent_of_job_request.delay')
    def test_create_booking(self, notify_parent, notify_sitter, get_time_zone):
        url = reverse.reverse('booking-list')
        response = self.client.post(url, self.data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
        assert_that(response.data.keys(), contains(*self.expected_properties))
        assert_that(notify_parent.call_count, is_(1))
        assert_that(notify_sitter.call_count, is_(self.parent.sitter_teams.count()))
        assert_that(get_time_zone.call_count, is_(1))

        booking = Booking.objects.get(pk=response.data.get('id'))
        assert_that(booking.time_zone, is_('America/New_York'))

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.tasks.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.tasks.notifications.notify_parent_of_job_request.delay')
    def test_update_booking(self, notify_parent, notify_sitter, get_time_zone):
        url = reverse.reverse('booking-list')
        response = self.client.post(url, self.data, format='json')
        assert_that(get_time_zone.call_count, is_(1))
        assert_that(notify_parent.call_count, is_(1))
        assert_that(notify_sitter.call_count, is_(self.parent.sitter_teams.count()))

        notify_parent.reset_mock()
        notify_sitter.reset_mock()

        detail_url = reverse.reverse('booking-detail', args=[response.data['id']])
        data = {'address2': 'Apt 3K'}
        self.client.patch(detail_url, data, format='json')
        assert_that(get_time_zone.call_count, is_(2))
        assert_that(notify_parent.call_count, is_(0))
        assert_that(notify_sitter.call_count, is_(0))

        data = {'starts_date_time': datetime.now()}
        self.client.patch(detail_url, data, format='json')
        assert_that(get_time_zone.call_count, is_(2))
        assert_that(notify_parent.call_count, is_(0))
        assert_that(notify_sitter.call_count, is_(0))
