# -*- coding: utf-8 -*-
import pytz

from django.utils import timezone

DEFAULT_TIMEZONE = 'America/New_York'


def get_timezone(timezone=None):
    return pytz.timezone(timezone) if timezone else pytz.timezone(DEFAULT_TIMEZONE)


def make_aware(value, timezone):
    return timezone.make_aware(value, timezone)


def now():
    return timezone.now()
