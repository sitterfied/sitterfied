# -*- coding: utf-8 -*-
import autofixture
import random

from hamcrest import assert_that, has_entry, is_
from rest_framework import reverse, status

from sitterfied.children.models import Child
from sitterfied.children.serializers import ChildSerializer
from sitterfied.test.testcases import SitterfiedApiTestCase, ViewSetTestCaseMixin


class TestViews(ViewSetTestCaseMixin, SitterfiedApiTestCase):

    expected_properties = ChildSerializer.Meta.fields

    class Meta:
        model = Child
        num_fixtures = 1

    def _get_create_data(self):
        if not hasattr(self, 'data'):
            self.parent = autofixture.create_one('app.Parent')
            self.data = {
                'dob': '2012-03-20',
                'name': 'Child One',
                'parent': self.parent.id,
            }
        return self.data

    def test_dob_formats(self):
        url = reverse.reverse('child-list')
        child = self.fixtures[0]
        parent = child.parent

        with self.login_with_user(parent.email):
            data = {
                'dob': '2012-03-20',
                'name': 'Child One',
                'parent': parent.id,
            }
            response = self.client.post(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))

            data.update(dob='2012-03-20T00:00:00.000Z')
            response = self.client.post(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))

    def test_update(self):
        child = random.choice(self.fixtures)

        with self.login_with_user(child.parent.email):
            data = {'name': 'Quinn'}
            response = self.client.patch(self.get_detail_url(child), data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('name', data['name']))
