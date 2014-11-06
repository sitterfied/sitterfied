# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from model_utils.models import TimeStampedModel
from pyuploadcare.dj import ImageField as UploadcareImageField

from sitterfied.app import intercom, us_states


class User(AbstractUser, TimeStampedModel):
    MEMBERSHIP_STATUS_PAID = 'paid'
    MEMBERSHIP_STATUS_TRIAL = 'trial'
    MEMBERSHIP_STATUS = (
        (MEMBERSHIP_STATUS_PAID, MEMBERSHIP_STATUS_PAID),
        (MEMBERSHIP_STATUS_TRIAL, MEMBERSHIP_STATUS_TRIAL),
    )

    objects = UserManager()

    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True, default='')
    avatar = UploadcareImageField(blank=True, manual_crop='174x174 upscale')
    cell = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=50, blank=True)
    facebook_id = models.IntegerField(null=True, blank=True, unique=True)
    facebook_token = models.CharField(max_length=256, null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)
    google_imported = models.BooleanField(default=False)
    invited_by = models.ManyToManyField('self', symmetrical=False, blank=True)
    languages = models.ManyToManyField('Language', blank=True, related_name='users')
    membership_exp_date = models.DateTimeField(null=True)
    users_in_network = models.ManyToManyField('self', blank=True, symmetrical=True)
    sitter_groups = models.ManyToManyField('Group', blank=True)
    state = models.CharField(choices=us_states.US_STATES, max_length=2, blank=True, default="AL")
    status = models.CharField(blank=False, max_length=10, choices=MEMBERSHIP_STATUS, default=MEMBERSHIP_STATUS_TRIAL)
    timezone = models.CharField(max_length=255, default='America/New_York', blank=True)
    zip = models.CharField(max_length=9, blank=True)  # there is

    @property
    def avatar_url(self):
        cdn_url = getattr(self.avatar, 'cdn_url', None)
        if cdn_url:
            return cdn_url.replace('http://www.ucarecdn.com/', settings.UPLOADCARE.get('upload_base_url'))
        return cdn_url

    @property
    def hash(self):
        if getattr(self, '_hash', None) is None:
            self._hash = intercom.generate_intercom_user_hash(self.email)
        return self._hash

    def is_facebook_connected(self):
        return self.facebook_id is not None

    def is_parent_or_sitter(self):
        if hasattr(self, 'sitter'):
            return 'Sitter'
        elif hasattr(self, 'parent'):
            return 'Parent'
        else:
            return 'Admin'

    @property
    def profile_completed(self):
        return False

    def __unicode__(self):
        return self.get_full_name()

    class Meta:
        app_label = 'app'


class Settings(TimeStampedModel):
    """
    User settings model

    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True)

    email_booking_accepted_denied = models.BooleanField(default=True)
    email_booking_request = models.BooleanField(default=True)
    email_blog = models.BooleanField(default=False)
    email_friend_joined = models.BooleanField(default=True)
    email_groups_added_network = models.BooleanField(default=True)
    email_new_review = models.BooleanField(default=True)
    email_news = models.BooleanField(default=False)
    email_upcoming_booking_remind = models.BooleanField(default=True)
    mobile_booking_accepted_denied = models.BooleanField(default=True)
    mobile_booking_request = models.BooleanField(default=True)
    mobile_friend_joined = models.BooleanField(default=True)
    mobile_groups_added_network = models.BooleanField(default=True)
    mobile_new_review = models.BooleanField(default=True)
    mobile_upcoming_booking_remind = models.BooleanField(default=True)

    class Meta:
        app_label = 'app'
