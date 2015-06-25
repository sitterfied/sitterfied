# -*- coding: utf-8 -*-
import autofixture

from hamcrest import assert_that, is_
from rest_framework import reverse, status

from sitterfied.utils.test import SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    def setUp(self):
        super(TestViews, self).setUp()

        self.parent = autofixture.get('app.Parent').create_one()

    def test_dob_formats(self):
        url = reverse.reverse('child-list')

        data = {
            'dob': '2012-03-20',
            'name': 'Child One',
            'parent': self.parent.id,
        }
        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))

        data.update(dob='2012-03-20T00:00:00.000Z')
        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
