# -*- coding: utf-8 -*-
import autofixture
import json
import random
import uuid

from datetime import timedelta
from delorean import Delorean
from django.utils import timezone
from hamcrest import all_of, assert_that, contains_string, has_entries, has_entry, has_key, is_, not_none
from mock import patch
from rest_framework import reverse, status
from rest_framework.authtoken.models import Token

from sitterfied.test.testcases import SitterfiedApiTestCase
from sitterfied.utils.time import get_today


class ViewsTestCase(SitterfiedApiTestCase):

    def setUp(self):
        super(ViewsTestCase, self).setUp()

        self.client.logout()

        self.user = autofixture.get('app.User').create_one()
        self.token = Token.objects.create(user=self.user)

        parent_fixture = autofixture.get('app.Parent')

        # No sitter team, no friends
        self.parent_one = parent_fixture \
            .update_generate_m2m({'children': (1, 3)}) \
            .create_one()

        # Sitter team
        self.parent_two = parent_fixture \
            .update_generate_m2m({'children': (1, 3), 'sitter_teams': (1, 1)}) \
            .create_one()

        # No sitter team, friends with sitters
        self.parent_three = parent_fixture \
            .update_generate_m2m({'children': (1, 3)}) \
            .create_one()

        # Make sure parent one has no friends
        self.parent_one.friends.clear()

        # Make sure parent three is friends with parent two
        self.parent_three.friends.add(self.parent_two)

    def test_booking_flow_requires_authentication(self):
        url = reverse.reverse('textit-booking-requests')
        response = self.client.post(url, {}, format='multipart')
        assert_that(response.status_code, is_(status.HTTP_401_UNAUTHORIZED))

        url = reverse.reverse('textit-booking-tier')
        response = self.client.post(url, {}, format='multipart')
        assert_that(response.status_code, is_(status.HTTP_401_UNAUTHORIZED))

    def test_booking_flow_requires_valid_data(self):
        url = '{}?token={}'.format(reverse.reverse('textit-booking-requests'), self.token.key)
        response = self.client.post(url, {}, format='multipart')
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST))

        url = '{}?token={}'.format(reverse.reverse('textit-booking-tier'), self.token.key)
        response = self.client.post(url, {}, format='multipart')
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST))

    def test_request_a_sitter(self):
        format = 'multipart'
        url = '{}?token={}'.format(reverse.reverse('textit-booking-requests'), self.token.key)
        relayer = random.randint(1000, 5000)
        flow_id = random.randint(1000, 5000)

        data = {
            'event': 'flow',
            'relayer': relayer,
            'relayer_phone': '+15555555555',
            'phone': self.parent_one.cell,
            'flow': flow_id,
            'step': str(uuid.uuid4()),
            'text': 'garbage',
            'time': timezone.now(),
            'values': '[]',
        }
        response = self.client.post(url, data, format=format)
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST), str(response.data))
        assert_that(response.data, has_entry('is_valid', False))

        today = get_today()
        data.update(text='find a sitter today from 9am-5pm', phone=self.parent_three.cell)
        response = self.client.post(url, data, format=format)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entries(
            is_valid=True,
            start_date='{dt:%a}, {dt:%b} {dt.day}'.format(dt=today),
            start_time='9:00am',
            end_date=not_none(),
            end_time='5:00pm',
        ))

        tomorrow = today + timedelta(days=1)
        data.update(text='find me a sitter tomorrow from 7pm-10pm', phone=self.parent_two.cell)
        response = self.client.post(url, data, format=format)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entries(
            is_valid=True,
            start_date='{dt:%a}, {dt:%b} {dt.day}'.format(dt=tomorrow),
            start_time='7:00pm',
            end_date=not_none(),
            end_time='10:00pm',
        ))

        # Delorean assumes the next friday to be the nearest upcoming friday
        next_friday = Delorean(today).next_friday()
        # NLP assumes next friday is the friday *after* the upcoming
        # friday, i.e., this friday
        data.update(text='need a sitter friday from 6-10pm')
        response = self.client.post(url, data, format=format)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entries(
            is_valid=True,
            start_date='{dt:%a}, {dt:%b} {dt.day}'.format(dt=next_friday.datetime),
            start_time='6:00pm',
            end_date=not_none(),
            end_time='10:00pm',
        ))

    @patch('sitterfied.integrations.textit.views.get_time_zone_for_zip', return_value='America/New_York')
    @patch('sitterfied.app.tasks.notifications.send_message')
    def test_determine_tier(self, send_message, time_zone):
        format = 'multipart'
        url = '{}?token={}'.format(reverse.reverse('textit-booking-tier'), self.token.key)
        relayer = random.randint(1000, 5000)
        flow_id = random.randint(1000, 5000)
        date = get_today() + timedelta(days=10)
        text = '{dt:%b} {dt.day} from 6-10pm'.format(dt=date)
        values = [{
            'category': 'Valid',
            'node': 'b06a3963-7e4b-46ae-9347-0ee42001e8d5',
            'time': '2015-03-16T17:20:05.156625Z',
            'text': text,
            'rule_value': 'True',
            'value': 'True',
            'label': 'is_valid',
        }]
        base_data = {
            'event': 'flow',
            'relayer': relayer,
            'relayer_phone': '+15555555555',
            'phone': self.parent_one.cell,
            'flow': flow_id,
            'step': str(uuid.uuid4()),
            'text': 'blah',
            'time': timezone.now(),
            'values': json.dumps(values),
        }

        response = self.client.post(url, base_data, format=format)
        assert_that(response.status_code, is_(status.HTTP_400_BAD_REQUEST), str(response.data))
        assert_that(response.data, has_key('detail'))

        # Parent 1 has no sitters and no friends with sitters so she
        # should be tier 3
        data = base_data.copy()
        data.update(text='YES')
        response = self.client.post(url, data, format=format)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entries(tier=3, num_sitters=self.parent_one.sitter_teams.count()))
        assert_that(send_message.call_count, is_(0))

        # Parent 2 has a sitter team so she should be tier 1
        data = data.copy()
        data.update(phone=self.parent_two.cell)
        response = self.client.post(url, data, format=format)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entries(tier=1, num_sitters=self.parent_two.sitter_teams.count()))
        # Should be called once for the sitter
        assert_that(send_message.call_count, is_(1))
        assert_that(send_message.call_args[1], has_entry('body',
            all_of(contains_string('{dt:%b} {dt.day}'.format(dt=date)), contains_string('6pm-10pm'))
        ))
        assert_that(time_zone.call_count, is_(1))

        send_message.reset_mock()

        # Parent 3 has a friend with a sitter team so she should be
        # tier 2
        data = data.copy()
        data.update(phone=self.parent_three.cell)
        response = self.client.post(url, data, format=format)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entries(tier=2, num_sitters=self.parent_two.sitter_teams.count()))
        assert_that(send_message.call_count, is_(0))
