# -*- coding: utf-8 -*-
import autofixture
import random
import string

from rest_framework.test import APITestCase

from sitterfied.utils.tests.autofixtures import *


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


class SitterfiedApiTestCase(APITestCase):

    def setUp(self):
        autofixture.create_one('app.User')

        self.login_with_staff_user()

    def login_with_staff_user(self):
        self.client.login(username='test@sitterfied.com', password='password')

    def login_with_random_user(self):
        user = autofixture.get('app.Parent').create_one()
        self.client.login(username=user.email, password='password')
        return user.username
