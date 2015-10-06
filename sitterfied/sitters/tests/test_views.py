# -*- coding: utf-8 -*-
import random

from datetime import date
from hamcrest import assert_that, has_entry, is_
from rest_framework import reverse, status

from sitterfied.sitters.models import Sitter
from sitterfied.sitters.serializers import SitterSerializer
from sitterfied.test.testcases import random_string, SitterfiedApiTestCase, ViewSetTestCaseMixin


class TestViews(ViewSetTestCaseMixin, SitterfiedApiTestCase):

    expected_properties = SitterSerializer.Meta.fields

    class Meta:
        model = Sitter

    def _get_create_data(self):
        username = random_string(8)
        return {
            'username': username,
            'first_name': random_string(5),
            'last_name': random_string(6),
            'bookmarks': [],
            'dob': '1990-01-01',
            'email': '{}@test.sitterfied.com'.format(username),
            'infant_exp': 1,
            'languages': [],
            'one_child_min_rate': 10,
            'one_child_max_rate': 20,
            'pre_teen_exp': 1,
            'preschool_exp': 1,
            'reviews': [],
            'school_age_exp': 1,
            'teen_exp': 3,
            'three_child_min_rate': 60,
            'three_child_max_rate': 70,
            'toddler_exp': 3,
            'total_Exp': 5,
            'two_child_min_rate': 30,
            'two_child_max_rate': 50,
            'total_exp': 10,

        }

    def test_address_change(self):
        sitter = random.choice(self.fixtures)

        with self.login_with_user(sitter.email, profile_type='sitter'):
            data = {'address1': '50 Main St'}
            url = reverse.reverse('sitter-detail', args=[sitter.id])
            response = self.client.patch(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))

    def test_dob_formats(self):
        sitter = random.choice(self.fixtures)

        with self.login_with_user(sitter.email, profile_type='sitter'):
            url = reverse.reverse('sitter-detail', args=[sitter.id])
            response = self.client.get(url)
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('dob', sitter.dob.date().strftime('%Y-%m-%d')))

            data = {'dob': '1988-03-20T00:00:00.000Z'}
            response = self.client.patch(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('dob', date(1988, 3, 20).strftime('%Y-%m-%d')))

    def test_update(self):
        sitter = random.choice(self.fixtures)

        with self.login_with_user(sitter.email, profile_type='sitter'):
            data = {'first_name': 'Genna'}
            url = reverse.reverse('sitter-detail', args=[sitter.id])
            response = self.client.patch(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('first_name', 'Genna'))
