# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from hamcrest import assert_that, contains, is_
from mock import patch
from rest_framework import reverse, status

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.parents.models import SitterTeamMembership
from sitterfied.utils.test import create_parents, create_sitters, SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    expected_properties = BookingSerializer.Meta.fields

    def setUp(self):
        super(TestViews, self).setUp()

        self.sitters = create_sitters(3)
        self.parent = create_parents(1)[0]

        for sitter in self.sitters:
            SitterTeamMembership.objects.create(parent=self.parent, sitter=sitter)

        starts = datetime.now()
        stops = starts + timedelta(hours=3)

        self.data = {
            'address1': '501 Adams St',
            'address2': 'Apt 2E',
            'city': 'Hoboken',
            'num_children': 1,
            'parent': self.parent.id,
            'start_date_time': starts,
            'state': 'NJ',
            'sitters': [sitter.id for sitter in self.sitters],
            'stop_date_time': stops,
            'zip': '07030',
        }

    @patch('sitterfied.app.signals.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.signals.notifications.notify_parent_of_job_request.delay')
    def test_create_booking(self, notify_parent, notify_sitter):
        url = reverse.reverse('booking-list')
        response = self.client.post(url, self.data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
        assert_that(response.data.keys(), contains(*self.expected_properties))
        assert_that(notify_parent.called, is_(True))
        assert_that(notify_sitter.call_count, is_(3))

        booking = Booking.objects.get(pk=response.data.get('id'))
        assert_that(booking.time_zone, is_('America/New_York'))

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    def test_update_booking(self, get_time_zone):
        url = reverse.reverse('booking-list')
        response = self.client.post(url, self.data, format='json')
        assert_that(get_time_zone.call_count, is_(1))

        booking_id = response.data.get('id')

        url = reverse.reverse('booking-detail', args=[booking_id])
        data = {'address2': 'Apt 3K'}
        self.client.patch(url, data, format='json')
        assert_that(get_time_zone.call_count, is_(2))

        data = {'starts_date_time': datetime.now()}
        self.client.patch(url, data, format='json')
        assert_that(get_time_zone.call_count, is_(2))
