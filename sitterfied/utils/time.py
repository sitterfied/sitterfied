# -*- coding: utf-8 -*-
import pytz
import requests

from django.conf import settings
from django.utils import timezone

DEFAULT_TIMEZONE = 'America/New_York'


def get_timezone(timezone=None):
    return pytz.timezone(timezone) if timezone else pytz.timezone(DEFAULT_TIMEZONE)


def get_time_zone_for_zip(zip_code, default='America/New_York'):
    request_url = 'http://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees'.format(
        api_key=settings.ZIP_CODE_API_KEY,
        zip_code=zip_code
    )
    response = requests.get(request_url)
    if response.status_code != 200:
        return default

    return response.json().get('timezone', {}).get('timezone_identifier', default)


def make_aware(value, tz):
    return timezone.make_aware(value, tz)


def now():
    return timezone.now()
