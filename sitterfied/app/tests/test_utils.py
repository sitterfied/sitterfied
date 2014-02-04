# -*- coding: utf-8 -*-
from app import utils
from hamcrest import *

def test_generate_short_url_code():
    code = utils.generate_short_url_code()
    assert_that(code, has_length(5))
    assert_that(code, matches_regexp('[a-zA-Z0-9]{5}'))
