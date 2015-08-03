# -*- coding: utf-8 -*-
import pytz
import requests

from datetime import datetime, timedelta
from django.conf import settings
from django.utils import timezone

from sitterfied.utils.decorators import memoized

DEFAULT_TIMEZONE = 'America/New_York'


def get_timezone(tz=None):
    return pytz.timezone(tz) if tz else pytz.timezone(DEFAULT_TIMEZONE)


@memoized
def get_time_zone_for_zip(zip_code, default='America/New_York'):
    request_url = 'http://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees'.format(
        api_key=settings.ZIP_CODE_API_KEY,
        zip_code=zip_code
    )
    response = requests.get(request_url)
    if response.status_code != 200:
        return default

    return response.json().get('timezone', {}).get('timezone_identifier', default)


def get_today(tz=None):
    """
    Retrieve a datetime representing today. Time zone specific.

    """
    return datetime.now(get_timezone(tz))


def is_dst(tz):
    time_zone = get_timezone(tz)
    now = pytz.utc.localize(datetime.utcnow())
    return now.astimezone(time_zone).dst() != timedelta(0)


def make_aware(value, tz):
    return timezone.make_aware(value, tz)


def now():
    return timezone.now()
