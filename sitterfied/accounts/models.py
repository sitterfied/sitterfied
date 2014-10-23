# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from model_utils.models import TimeStampedModel
from pyuploadcare import dj as pyuploadcare

from sitterfied.app import us_states
from sitterfied.app.intercom import generate_intercom_user_hash


class Account(AbstractUser, TimeStampedModel):
    objects = UserManager()

    MEMBERSHIP_STATUS_PAID = 'paid'
    MEMBERSHIP_STATUS_TRIAL = 'trial'
    MEMBERSHIP_STATUS = (
        (MEMBERSHIP_STATUS_PAID, MEMBERSHIP_STATUS_PAID),
        (MEMBERSHIP_STATUS_TRIAL, MEMBERSHIP_STATUS_TRIAL),
    )

    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, default='', blank=True)
    avatar = pyuploadcare.ImageField(manual_crop='175x174 upscale', blank=True)
    cell = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=50, blank=True)
    facebook_id = models.IntegerField(unique=True, null=True, blank=True)
    facebook_token = models.CharField(max_length=256, null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)
    google_imported = models.BooleanField(default=False)
    invited_by = models.ManyToManyField('self', related_name='+', symmetrical=False, blank=True)
    languages = models.ManyToManyField('Language', blank=True, related_name='users')
    membership_exp_data = models.DateTimeField(null=True)
    sitter_groups = models.ManyToManyField('Group', blank=True)
    state = models.CharField(max_length=2, choices=us_states.US_STATES, default='NJ', blank=True)
    status = models.CharField(max_length=10, choices=MEMBERSHIP_STATUS, default=MEMBERSHIP_STATUS_TRIAL, blank=True)
    timezone = models.CharField(max_length=255, blank=True)
    users_in_network = models.ManyToManyField('self', related_name='+', symmetrical=False, blank=True)
    zip = models.CharField(max_length=9, blank=True)

    @property
    def avatar_url(self):
        cdn_url = getattr(self.avatar, 'cdn_url', None)
        if cdn_url:
            return cdn_url.replace('http://www.ucarecdn.com/', settings.UPLOAD.get('upload_base_url'))

    @property
    def hash(self):
        if getattr(self, '_hash', None) is None:
            self._hash = generate_intercom_user_hash(self.email)
        return self._hash

    def is_facebook_connected(self):
        return self.facebook_id is not None

    def is_parent_or_sitter(self):
        if hasattr(self, 'parent'):
            return 'Parent'
        elif hasattr(self, 'sitter'):
            return 'Sitter'
        else:
            return 'Admin'

    @property
    def profile_completed(self):
        return False

    def __str__(self):
        return self.get_full_name()
