# -*- coding: utf-8 -*-
import pytz

from django.utils import timezone

DEFAULT_TIMEZONE = 'America/New_York'


def get_timezone(timezone=None):
    return pytz.timezone(timezone) if timezone else pytz.timezone(DEFAULT_TIMEZONE)


def make_aware(value, tz):
    return timezone.make_aware(value, tz)


def now():
    return timezone.now()
