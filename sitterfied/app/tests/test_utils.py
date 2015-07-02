# -*- coding: utf-8 -*-
from django.conf import settings
from django.test import TestCase
from hamcrest import assert_that, has_length, matches_regexp
from unittest import skip

from sitterfied.app import utils


@skip
class UtilsTestCase(TestCase):

    def test_generate_short_url_code(self):
        code = utils.generate_short_url_code()
        assert_that(code, has_length(5))
        assert_that(code, matches_regexp('[a-zA-Z0-9]{5}'))

    def test_get_short_url(self):
        url = utils.get_short_url('/path')
        assert_that(url, matches_regexp(settings.SHORT_URL + '[a-zA-Z0-9]{5}'))
