# -*- coding: utf-8 -*-
import mock
import requests

from django.test import TestCase
from hamcrest import all_of, assert_that, is_, is_not, none, not_none
from unittest import skip

from sitterfied.app import tasks
from sitterfied.users.models import User


@skip
class TasksTestCase(TestCase):

    def test_geocode_user(self):
        with mock.patch('app.tasks.geocoders') as mock_geocoders:
            with mock.patch.object(User.objects, 'get') as mock_user_get:
                mock_user_get.return_value = mock_user = mock.Mock(spec=User)
                mock_user.id = 1
                mock_user.zip = '07030'

                mock_geocoders.GoogleV3.return_value.geocode.return_value = ('Hoboken, NJ 07030', ('55', '33'))
                lat, lng = tasks.geocode_user(1)
                assert_that(lat, all_of(not_none(), is_not('')))
                assert_that(lng, all_of(not_none(), is_not('')))

    def test_geocode_user_does_not_exist(self):
        with mock.patch.object(User.objects, 'get') as mock_user_get:
            mock_user_get.side_effect = User.DoesNotExist

            assert_that(tasks.geocode_user(1), none())

    def test_geocode_user_no_zip(self):
        with mock.patch.object(User.objects, 'get') as mock_user_get:
            mock_user_get.return_value = mock_user = mock.Mock(spec=User)
            mock_user.zip = ''

            assert_that(tasks.geocode_user(1), none())

    def test_lookup_time_zone(self):
        with mock.patch.object(User.objects, 'get') as mock_user_get:
            mock_user_get.return_value = mock_user = mock.Mock(spec=User)
            mock_user.id = 1
            mock_user.zip = '07030'
            mock_user.timezone = ''

            with mock.patch.object(requests, 'get') as mock_get:
                mock_get.return_value = return_value = mock.Mock()
                return_value.json.return_value = {'timeZoneId': 'America/New_York'}

                assert_that(tasks.lookup_time_zone(('', ''), 1), is_('America/New_York'))

    def test_lookup_time_zone_no_lat_long(self):
        assert_that(tasks.lookup_time_zone((), 1), none())

    def test_lookup_time_zone_user_does_not_exist(self):
        with mock.patch.object(User.objects, 'get') as mock_user_get:
            mock_user_get.side_effect = User.DoesNotExist

            assert_that(tasks.lookup_time_zone(('', ''), 1), none())

    def test_lookup_time_zone_user_has_timezone(self):
        with mock.patch.object(User.objects, 'get') as mock_user_get:
            mock_user_get.return_value = mock_user = mock.Mock(spec=User)
            mock_user.id = 1
            mock_user.zip = '07030'
            mock_user.timezone = 'America/New_York'

            assert_that(tasks.lookup_time_zone(('', ''), 1), none())

    def test_lookup_time_zone_cannot_save_user(self):
        with mock.patch.object(User.objects, 'get') as mock_user_get:
            mock_user_get.return_value = mock_user = mock.Mock(spec=User)
            mock_user.id = 1
            mock_user.zip = '07030'
            mock_user.timezone = ''
            mock_user.save.side_effect = Exception

            with mock.patch.object(requests, 'get') as mock_get:
                mock_get.return_value = return_value = mock.Mock()
                return_value.json.return_value = {'timeZoneId': 'America/New_York'}

                assert_that(tasks.lookup_time_zone(('', ''), 1), none())
