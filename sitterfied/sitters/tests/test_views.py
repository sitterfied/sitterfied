# -*- coding: utf-8 -*-
from hamcrest import assert_that, is_
from rest_framework import reverse, status

from sitterfied.utils.test import SitterfiedApiTestCase, random_string


class TestViews(SitterfiedApiTestCase):

    def test_dob_formats(self):
        url = reverse.reverse('sitter-list')

        data = {
            'dob': '2012-03-20',
            'email': 'sitter.one@sitterfied.com',
            'first_name': 'Sitter',
            'last_name': 'One',
            'password': 'password',
            'total_exp': 1,
            'pre_teen_exp': 1,
            'preschool_exp': 1,
            'teen_exp': 1,
            'special_needs_exp': 1,
            'school_age_exp': 1,
            'toddler_exp': 1,
            'infant_exp': 1,
            'one_child_max_rate': 10,
            'one_child_min_rate': 10,
            'two_child_max_rate': 10,
            'two_child_min_rate': 10,
            'three_child_min_rate': 10,
            'three_child_max_rate': 10,
            'schedule': 1,
            'settings': 1,
            'username': random_string(8),
        }
        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))

        data.update(dob='2012-03-20T00:00:00.000Z')
        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
