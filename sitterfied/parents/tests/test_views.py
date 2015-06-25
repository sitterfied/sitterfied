# -*- coding: utf-8 -*-
import autofixture
import random

from hamcrest import assert_that, contains, has_entries, has_entry, has_items, is_, none
from rest_framework import status
from rest_framework.reverse import reverse

from sitterfied.parents.serializers import ParentSerializer
from sitterfied.utils.test import random_string, SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    expected_properties = ParentSerializer.Meta.fields

    def setUp(self):
        super(TestViews, self).setUp()

        self.parents = autofixture.get('app.Parent').create(5)

    def test_create_parent(self):
        username = random_string(8)
        data = {
            'username': username,
            'first_name': random_string(5),
            'last_name': random_string(6),
            'email': '{}@sitterfied.com'.format(username),
        }
        url = reverse('parent-list')
        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
        assert_that(response.data.keys(), contains(*self.expected_properties))

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

        response = self.client.post(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
        assert_that(response.data, has_entry('sitter_teams', has_items(*sitter_ids)))

    def test_list_parents(self):
        url = reverse('parent-list')
        response = self.client.get(url)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(len(response.data), is_(len(self.parents)))

    def test_retrieve_parent(self):
        parent = random.choice(self.parents)
        url = reverse('parent-detail', args=[parent.id])
        response = self.client.get(url)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data.keys(), contains(*self.expected_properties))
        assert_that(response.data, has_entries(
            username=parent.username,
            first_name=parent.first_name,
            last_name=parent.last_name,
            email=parent.email,
        ))

    def test_delete_parent(self):
        parent = random.choice(self.parents)
        url = reverse('parent-detail', args=[parent.id])
        response = self.client.delete(url)
        assert_that(response.status_code, is_(status.HTTP_204_NO_CONTENT), str(response.data))
        assert_that(response.data, none())

    def test_update_parent(self):
        sitters = autofixture.get('app.Sitter').create(10)
        sitter_ids = [sitter.id for sitter in sitters]

        parent = random.choice(self.parents)
        data = {'sitter_teams': sitter_ids}
        url = reverse('parent-detail', args=[parent.id])
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('sitter_teams', has_items(*sitter_ids)))

        data.update({'sitter_teams': None})
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('sitter_teams', []))

        data.update({'sitter_teams': []})
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('sitter_teams', []))
