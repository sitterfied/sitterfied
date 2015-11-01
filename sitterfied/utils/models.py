# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel

from sitterfied.db.fields import CaseInsensitiveCharField


class Certification(TimeStampedModel):
    """
    Certification model

    """
    certification = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.certification

    class Meta:
        app_label = 'app'


class Group(TimeStampedModel):
    """
    Group model

    """
    name = CaseInsensitiveCharField(max_length=128, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'app'


class IncomingSMSMessage(TimeStampedModel):
    """
    Incoming SMS Message model

    """
    body = models.CharField(max_length=161)
    date_created = models.DateTimeField()
    date_sent = models.DateTimeField()
    date_updated = models.DateTimeField()
    sid = models.CharField(max_length=34)
    status = models.CharField(max_length=12)
    to = models.CharField(max_length=16)

    def __unicode__(self):
        return self.sid

    class Meta:
        app_label = 'app'


class Language(TimeStampedModel):
    """
    Language model

    """
    language = models.CharField(max_length=100)

    def __unicode__(self):
        return self.language

    class Meta:
        app_label = 'app'


class OtherService(TimeStampedModel):
    """
    Other Service model

    """
    service = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.service

    class Meta:
        app_label = 'app'


class SpecialNeed(TimeStampedModel):
    """
    Special Need model

    """
    need = models.CharField(max_length=100)

    def __unicode__(self):
        return self.need

    class Meta:
        app_label = 'app'


class WatchedFieldsMixin(models.Model):
    """
    This mixin provides a means of "watching" model fields for changes.

    """
    _watched_fields = []

    def __init__(self, *args, **kwargs):
        super(WatchedFieldsMixin, self).__init__(*args, **kwargs)

        for field in self._watched_fields:
            setattr(self, '__original_{}'.format(field), getattr(self, field))

    def field_has_changed(self, field):
        if field in self._watched_fields:
            return getattr(self, '__original_{}'.format(field)) != getattr(self, field)
        return False

    def get_original_value(self, field):
        return getattr(self, '__original_{}'.format(field), None)

    def has_changed(self):
        for field in self._watched_fields:
            if self.field_has_changed(field):
                return True

        return False

    class Meta:
        abstract = True
