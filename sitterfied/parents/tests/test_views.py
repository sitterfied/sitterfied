# -*- coding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save, Signal
from hamcrest import assert_that, has_entries, has_entry, contains, is_, none
from rest_framework import status
from rest_framework.reverse import reverse

from sitterfied.app import signals
from sitterfied.parents.models import Parent
from sitterfied.parents.serializers import ParentSerializer
from sitterfied.sitters.models import Sitter
from sitterfied.utils.test import create_sitters, random_string, SitterfiedApiTestCase


class TestViews(SitterfiedApiTestCase):

    expected_properties = ParentSerializer.Meta.fields

    def setUp(self):
        super(TestViews, self).setUp()

        Signal.disconnect(post_save, receiver=signals.new_parent, sender=Parent)

        parent = Parent.objects.create(
            email='parentone@sitterfied.com',
            username='parentone',
            first_name='Parent',
            last_name='One',
            password=make_password('password'),
        )
        self.parent_id = parent.id

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

        create_sitters(2)

        sitter_ids = Sitter.objects.values_list('id', flat=True)
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
        assert_that(response.data, has_entry('sitter_teams', list(sitter_ids)))

    def test_list_parents(self):
        url = reverse('parent-list')
        response = self.client.get(url)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(len(response.data), is_(1))

    def test_retrieve_parent(self):
        url = reverse('parent-detail', args=[self.parent_id])
        response = self.client.get(url)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data.keys(), contains(*self.expected_properties))
        assert_that(response.data, has_entries(
            username='parentone',
            first_name='Parent',
            last_name='One',
            email='parentone@sitterfied.com',
        ))

    def test_delete_parent(self):
        url = reverse('parent-detail', args=[self.parent_id])
        response = self.client.delete(url)
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, none())

    def test_update_parent(self):
        create_sitters(10)
        sitter_ids = Sitter.objects.values_list('id', flat=True)

        data = {
            'sitter_teams': sitter_ids,
        }

        url = reverse('parent-detail', args=[self.parent_id])
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('sitter_teams', list(sitter_ids)))

        data.update({'sitter_teams': None})
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('sitter_teams', []))

        data.update({'sitter_teams': []})
        response = self.client.patch(url, data, format='json')
        assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
        assert_that(response.data, has_entry('sitter_teams', []))
