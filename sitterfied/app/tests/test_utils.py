# -*- coding: utf-8 -*-
from django.conf import settings
from hamcrest import *

from app import utils


def test_generate_short_url_code():
    code = utils.generate_short_url_code()
    assert_that(code, has_length(5))
    assert_that(code, matches_regexp('[a-zA-Z0-9]{5}'))


def test_get_short_url():
    url = utils.get_short_url('/path')
    assert_that(url, matches_regexp(settings.SHORT_URL + '[a-zA-Z0-9]{5}'))
