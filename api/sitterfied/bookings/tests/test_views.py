# -*- coding: utf-8 -*-
import autofixture

from datetime import datetime, timedelta
from hamcrest import assert_that, only_contains, has_entry, has_items, is_
from mock import patch
from rest_framework import reverse, status

from sitterfied.bookings.models import Booking
from sitterfied.bookings.serializers import BookingSerializer
from sitterfied.test.testcases import SitterfiedApiTestCase, ViewSetTestCaseMixin


class TestViews(ViewSetTestCaseMixin, SitterfiedApiTestCase):

    expected_properties = BookingSerializer.Meta.fields

    class Meta:
        model = Booking
        num_fixtures = 5

    def _get_create_data(self):
        if not hasattr(self, 'data'):
            self.parent = autofixture.create_one('app.Parent')
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
        return self.data

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.signals.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.signals.notifications.notify_parent_of_job_request.delay')
    def setUp(self, notify_parent, notify_sitter, get_time_zone):
        super(TestViews, self).setUp()

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.signals.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.signals.notifications.notify_parent_of_job_request.delay')
    def test_create(self, notify_parent, notify_sitter, get_time_zone):
        super(TestViews, self).test_create()

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.signals.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.signals.notifications.notify_parent_of_job_request.delay')
    def test_create_with_sitters(self, notify_parent, notify_sitter, get_time_zone):
        parent = 'parent@test.sitterfied.com'

        with self.login_with_user(parent):
            url = reverse.reverse('booking-list')
            response = self.client.post(url, self._get_create_data(), format='json')
            assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
            data = response.data

        with self.login_with_user(parent):
            response = self.client.get(response['Location'])
            assert_that(response.data, has_entry('sitters', has_items(*data['sitters'])))
            assert_that(notify_parent.call_count, is_(1))
            assert_that(notify_sitter.call_count, is_(self.parent.sitter_teams.count()))
            assert_that(get_time_zone.call_count, is_(1))

            booking = Booking.objects.get(pk=response.data.get('id'))
            assert_that(booking.time_zone, is_('America/New_York'))

    @patch('sitterfied.utils.time.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.tasks.notifications.notify_sitter_of_job_request.delay')
    @patch('sitterfied.app.tasks.notifications.notify_parent_of_job_request.delay')
    def test_update(self, notify_parent, notify_sitter, get_time_zone):
        create_data = self._get_create_data()

        with self.login_with_user():
            url = reverse.reverse('booking-list')
            response = self.client.post(url, create_data, format='json')
            assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
            assert_that(response.data, has_entry('sitters', has_items(*create_data['sitters'])))
            assert_that(get_time_zone.call_count, is_(1))
            assert_that(notify_parent.call_count, is_(1))
            assert_that(notify_sitter.call_count, is_(self.parent.sitter_teams.count()))

            notify_parent.reset_mock()
            notify_sitter.reset_mock()

            detail_url = reverse.reverse('booking-detail', args=[response.data['id']])
            data = {'address2': 'Apt 3K', 'sitters': create_data['sitters'][0:1]}
            response = self.client.patch(detail_url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data.keys(), only_contains(*self.expected_properties))
            assert_that(response.data, has_entry('sitters', has_items(*data['sitters'])))
            assert_that(get_time_zone.call_count, is_(2))
            assert_that(notify_parent.call_count, is_(0))
            assert_that(notify_sitter.call_count, is_(0))

            data = {'starts_date_time': datetime.now()}
            self.client.patch(detail_url, data, format='json')
            assert_that(get_time_zone.call_count, is_(2))
            assert_that(notify_parent.call_count, is_(0))
            assert_that(notify_sitter.call_count, is_(0))

            data = {'sitters': []}
            response = self.client.patch(detail_url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('sitters', is_([])))

            data = {'sitters': create_data['sitters']}
            response = self.client.patch(detail_url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('sitters', has_items(*data['sitters'])))
            assert_that(notify_parent.call_count, is_(0))
            assert_that(notify_sitter.call_count, is_(len(data['sitters'])))
