# -*- coding: utf-8 -*-
import autofixture
import random

from datetime import date
from hamcrest import assert_that, has_entry, is_
from rest_framework import reverse, status

from sitterfied.utils.test import SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    def setUp(self):
        super(TestViews, self).setUp()

        self.sitters = autofixture.get('app.Sitter').create(5)

    def test_dob_formats(self):
        sitter = random.choice(self.sitters)
        url = reverse.reverse('sitter-detail', args=[sitter.id])
        response = self.client.get(url)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('dob', sitter.dob.date()))

        data = {'dob': '1988-03-20T00:00:00.000Z'}
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('dob', date(1988, 3, 20)))

    def test_address_change(self):
        sitter = random.choice(self.sitters)
        data = {'address1': '50 Main St'}
        url = reverse.reverse('sitter-detail', args=[sitter.id])
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
