# -*- coding: utf-8 -*-
import os
import unittest

from hamcrest import assert_that, is_

os.environ['DOTCLOUD_DATA_SQL_HOST'] = '127.0.0.1'
os.environ['DOTCLOUD_DATA_SQL_PORT'] = '5432'
os.environ['DOTCLOUD_DATA_SQL_LOGIN'] = 'vagrant'
os.environ['DOTCLOUD_DATA_SQL_PASSWORD'] = 'vagrant'

import knowtify


class TestKnowtify(unittest.TestCase):

    def setUp(self):
        super(TestKnowtify, self).setUp()

    def test_main(self):
        print(knowtify.main())
