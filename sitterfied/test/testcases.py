# -*- coding: utf-8 -*-
import autofixture
import random
import string

from contextlib import contextmanager
from hamcrest import assert_that, is_, none, not_none, only_contains
from rest_framework import reverse, status
from rest_framework.test import APITestCase

from sitterfied.parents.models import Parent
from sitterfied.sitters.models import Sitter
from sitterfied.test.autofixtures import *
from sitterfied.users.models import User


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


class SitterfiedApiTestCase(APITestCase):

    @contextmanager
    def login_with_user(self, email=None, profile_type='parent', **kwargs):
        """
        Login with a given username, profile type, and profile arguments.

        To be used as a context manager, yields the created or retrieved
        profile. Extra kwargs will be passed to the profile constructor.
        """
        email = email or random_string(10) + '@test.sitterfied.com'

        profile_class = {
            'parent': Parent,
            'sitter': Sitter,
        }[profile_type.lower()]

        if not User.objects.filter(email=email).exists():
            field_values = {
                'email': email,
                'password': make_password('password'),
            }
            field_values.update(**kwargs)
            fixture_name = 'app.{}'.format(profile_type.title())
            profile = autofixture.create_one(fixture_name, field_values=field_values)
        else:
            profile = profile_class.objects.get(email=email)
            if kwargs:
                for key, value in kwargs.items():
                    assert getattr(profile, key) == value, "kwarg passed to login that is not valid on profile"

        assert self.client.login(username=email, password='password')
        self.client.credentials(HTTP_REFERER='http://dev.sitterfied.com')

        yield profile

        self.client.logout()


class ViewSetTestCaseMixin(object):

    def setUp(self):
        """
        Generate test fixtures.

        """
        app_label = self.__class__.Meta.model._meta.app_label
        app_name = self.__class__.Meta.model.__name__.lower()
        model_name = '{}.{}'.format(app_label, app_name.title())
        num_fixtures = getattr(self.__class__.Meta, 'num_fixtures', 5)

        self.fixtures = autofixture.create(model_name, count=num_fixtures)
        self.model = self.__class__.Meta.model
        self.profile_type = app_name if app_name in ['parent', 'sitter'] else 'parent'
        self.view_name_base = app_name

    def _get_create_data(self):
        raise NotImplementedError('_get_create_data method must be implemented by sub-classes')

    def get_detail_url(self, param):
        return reverse.reverse('{}-detail'.format(self.view_name_base), args=[param.id])

    def get_list_url(self):
        return reverse.reverse('{}-list'.format(self.view_name_base))

    def test_create(self):
        with self.login_with_user(profile_type=self.profile_type):
            data = self._get_create_data()
            response = self.client.post(self.get_list_url(), data, format='json')
            assert_that(response.status_code, is_(status.HTTP_201_CREATED), str(response.data))
            assert_that(response.data.keys(), only_contains(*self.expected_properties))
            assert_that(response['Location'], not_none())

    def test_delete(self):
        object = random.choice(self.fixtures)
        with self.login_with_user(profile_type=self.profile_type):
            response = self.client.delete(self.get_detail_url(object))
            assert_that(response.status_code, is_(status.HTTP_204_NO_CONTENT), str(response.data))
            assert_that(response.data, none())

    def test_list(self):
        with self.login_with_user(profile_type=self.profile_type):
            response = self.client.get(self.get_list_url())
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(len(response.data), is_(self.model.objects.count()))

    def test_retrieve(self):
        object = random.choice(self.fixtures)
        with self.login_with_user(profile_type=self.profile_type):
            response = self.client.get(self.get_detail_url(object))
            assert_that(response.status_code, is_(status.HTTP_200_OK), str(response.data))
            assert_that(response.data.keys(), only_contains(*self.expected_properties))

    def test_update(self):
        raise NotImplementedError('test_update must be implemented by sub-classes')
