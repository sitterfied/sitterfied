# -*- coding: utf-8 -*-
import mock

from app.middleware import TimezoneMiddleware
from app.models import User
from django.test.client import RequestFactory
from hamcrest import *

def test_timezone_middleware():
    request = RequestFactory().get('/')
    request.user = mock.Mock(spec=User)
    request.user.is_authenticated.return_value = True
    request.user.zip = '07030'
    request.user.timezone = None

    middleware = TimezoneMiddleware()
    middleware.process_request(request)

    assert_that(request.user.timezone, is_('America/New_York'))

def test_timezone_middleware_no_location_found():
    request = RequestFactory().get('/')
    request.user = mock.Mock(spec=User)
    request.user.is_authenticated.return_value = True
    request.user.zip = '00000'
    request.user.timezone = None

    with mock.patch('app.middleware.geocoders') as mock_geocoders:
        mock_geocoders.GoogleV3.geocode.side_effect = Exception

        middleware = TimezoneMiddleware()
        middleware.process_request(request)

        assert_that(request.user.timezone, none())

def test_timezone_middleware_no_timezone_found():
    request = RequestFactory().get('/')
    request.user = mock.Mock(spec=User)
    request.user.is_authenticated.return_value = True
    request.user.zip = '00000'
    request.user.timezone = None

    with mock.patch('app.middleware.tzwhere') as mock_tzwhere:
        mock_tzwhere.tzNameAt.side_effect = Exception

        middleware = TimezoneMiddleware()
        middleware.process_request(request)

        assert_that(request.user.timezone, none())

def test_timezone_middleware_could_not_save():
    request = RequestFactory().get('/')
    request.user = mock.Mock(spec=User)
    request.user.is_authenticated.return_value = True
    request.user.zip = '07030'
    request.user.timezone = None
    request.user.save.side_effect = Exception

    with mock.patch('app.middleware.timezone') as mock_timezone:
        middleware = TimezoneMiddleware()
        middleware.process_request(request)

        assert_that(request.user.timezone, is_('America/New_York'))
        assert_that(mock_timezone.activate.called, is_(True))

def test_timezone_middleware_could_not_activate():
    request = RequestFactory().get('/')
    request.user = mock.Mock(spec=User)
    request.user.is_authenticated.return_value = True
    request.user.zip = '07030'
    request.user.timezone = None
    request.user.save.side_effect = Exception

    with mock.patch('app.middleware.timezone') as mock_timezone:
        mock_timezone.activate.side_effect = Exception

        middleware = TimezoneMiddleware()
        middleware.process_request(request)

        assert_that(request.user.timezone, none())
