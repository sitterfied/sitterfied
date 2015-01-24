# -*- coding: utf-8 -*-
import random
import string

from datetime import date
from django.db.models.signals import post_save, Signal
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase

from sitterfied.app import signals
from sitterfied.sitters.models import Sitter
from sitterfied.utils import time


def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def create_sitters(count=10):
    Signal.disconnect(post_save, receiver=signals.new_sitter, sender=Sitter)

    sitters = []
    for _ in range(count):
        username = random_string(8)
        current_year = time.now().year - 18
        year = random.randrange(current_year - 65, current_year - 18)
        sitter = Sitter.objects.create(
            dob=date(year, random.randrange(1, 12), random.randrange(1, 28)),
            email='{}@sitterfied.com'.format(username),
            username=username,
            first_name=random_string(8),
            last_name=random_string(10),
            password=make_password('password'),
            total_exp=1,
            pre_teen_exp=1,
            preschool_exp=1,
            teen_exp=1,
            special_needs_exp=1,
            school_age_exp=1,
            toddler_exp=1,
            infant_exp=1,
            one_child_max_rate=10,
            one_child_min_rate=10,
            two_child_max_rate=10,
            two_child_min_rate=10,
            three_child_max_rate=10,
            three_child_min_rate=10,
        )
        sitters.append(sitter)

    Signal.connect(post_save, receiver=signals.new_sitter, sender=Sitter)

    return sitters


class SitterfiedApiTestCase(APITestCase):

    def setUp(self):
        UserModel = get_user_model()
        UserModel._default_manager.create(
            username='test',
            email='test@sitterfied.com',
            first_name='Test',
            last_name='Testerson',
            password=make_password('password'),
            is_staff=True
        )

        self.login_with_staff_user()

    def login_with_staff_user(self):
        self.client.login(username='test@sitterfied.com', password='password')

    def login_with_random_user(self):
        random_username = random_string(10)
        UserModel = get_user_model()
        user = UserModel._default_manager.create(
            username=random_username,
            email='{}@sitterfied.com'.format(random_username),
            first_name=random_string(5),
            last_name=random_string(8),
            password=make_password('password'),
        )

        self.client.login(username=user.email, password='password')
        return random_username
