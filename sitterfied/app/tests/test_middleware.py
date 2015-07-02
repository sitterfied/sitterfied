# -*- coding: utf-8 -*-
import mock

from django.test import TestCase
from django.test.client import RequestFactory
from hamcrest import assert_that, is_

from sitterfied.app.middleware import TimezoneMiddleware
from sitterfied.users.models import User


class MiddlewareTestCase(TestCase):

    def test_timezone_middleware(self):
        request = RequestFactory().get('/')
        request.user = mock.Mock(spec=User)
        request.user.is_authenticated.return_value = True
        request.user.zip = '07030'
        request.user.timezone = 'America/New_York'

        middleware = TimezoneMiddleware()
        middleware.process_request(request)

        assert_that(request.user.timezone, is_('America/New_York'))
