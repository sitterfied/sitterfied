# -*- coding: utf-8 -*-
import autofixture
import random

from hamcrest import assert_that, has_entry, has_items, is_, only_contains
from rest_framework import status
from rest_framework.reverse import reverse

from sitterfied.parents.models import Parent
from sitterfied.parents.serializers import ParentSerializer
from sitterfied.test.testcases import random_string, SitterfiedApiTestCase, ViewSetTestCaseMixin


class TestViews(ViewSetTestCaseMixin, SitterfiedApiTestCase):

    expected_properties = ParentSerializer.Meta.fields

    class Meta:
        model = Parent

    def _get_create_data(self):
        username = random_string(8)
        return {
            'username': username,
            'first_name': random_string(5),
            'last_name': random_string(6),
            'email': '{}@test.sitterfied.com'.format(username),
        }

    def test_create_with_sitter_team(self):
        with self.login_with_user():
            sitters = autofixture.get('app.Sitter').create(2)
            sitter_ids = [sitter.id for sitter in sitters]
            username = random_string(8)
            data = {
                'username': username,
                'first_name': random_string(5),
                'last_name': random_string(6),
                'email': '{}@sitterfied.com'.format(username),
                'sitter_teams': sitter_ids,
            }

            url = reverse('parent-list')
            response = self.client.post(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
            assert_that(response.data, has_entry('sitter_teams', has_items(*sitter_ids)))

    def test_update(self):
        sitters = autofixture.create('app.Sitter', 10)
        sitter_ids = [sitter.id for sitter in sitters]

        parent = random.choice(self.fixtures)
        data = {'sitter_teams': sitter_ids}
        url = reverse('parent-detail', args=[parent.id])

        with self.login_with_user(parent.email):
            response = self.client.patch(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data.keys(), only_contains(*self.expected_properties))
            assert_that(response.data, has_entry('sitter_teams', has_items(*sitter_ids)))

            data.update({'sitter_teams': sitter_ids[3:6]})
            response = self.client.patch(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('sitter_teams', has_items(*sitter_ids[3:6])))

            data.update({'sitter_teams': []})
            response = self.client.patch(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('sitter_teams', []))

            data.update({'sitter_teams': sitter_ids[7:]})
            response = self.client.patch(url, data, format='json')
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data, has_entry('sitter_teams', has_items(*sitter_ids[7:])))
