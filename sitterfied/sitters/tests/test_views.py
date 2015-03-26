# -*- coding: utf-8 -*-
from datetime import date
from hamcrest import assert_that, has_entry, is_
from rest_framework import reverse, status

from sitterfied.utils.test import SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    def test_dob_formats(self):
        url = '/onboarding2/'

        response = self.client.get(url)
        csrftoken = response.cookies.get('csrftoken')
        self.client.credentials(HTTP_X_CSRFTOKEN=csrftoken.value)

        data = {
            'address1': '1 Main St',
            'avatar': 'http://www.ucarecdn.com/69485f01-a288-4de7-8c16-da671c8fbe1f/',
            'parent_or_sitter': 'sitter',
            'biography': 'Awesomeness',
            'cell': '+15555555555',
            'city': 'Smallville',
            'dob': '1990-03-20',
            'email': 'sitter.one@sitterfied.com',
            'first_name': 'Sitter',
            'gender': 'female',
            'last_name': 'One',
            'password1': 'password',
            'password2': 'password',
            'total_exp': 1,
            'pre_teen_exp': 1,
            'preschool_exp': 1,
            'teen_exp': 1,
            'special_needs_exp': 1,
            'school_age_exp': 1,
            'state': 'KS',
            'toddler_exp': 1,
            'infant_exp': 1,
            'one_child_max_rate': 10,
            'one_child_min_rate': 10,
            'two_child_max_rate': 10,
            'two_child_min_rate': 10,
            'three_child_min_rate': 10,
            'three_child_max_rate': 10,
            'tos': True,
            'zip': 55555,
        }
        response = self.client.post(url, data, format='multipart')
        assert_that(response.status_code, is_(status.HTTP_302_FOUND))

        url = reverse.reverse('sitter-detail', args=[2])
        response = self.client.get(url)
        assert_that(response.status_code, is_(status.HTTP_200_OK))
        assert_that(response.data, has_entry('dob', date(1990, 3, 20)))

        data.update(dob='1988-03-20T00:00:00.000Z')
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK))
        assert_that(response.data, has_entry('dob', date(1988, 3, 20)))
