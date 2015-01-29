# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.utils import timezone
from geopy.geocoders import OpenCage

__all__ = [
    'TimezoneMiddleware'
]

logger = logging.getLogger('app.middleware')
geolocator = OpenCage(settings.OPEN_CAGE_API_KEY)


class TimezoneMiddleware(object):
    """
    Activate the current user's time zone at the start of a request.

    If the user does not have a time zone set, geocode the user and set time zone.

    """
    def process_request(self, request):
        if request.user.is_authenticated():
            user_timezone = request.user.timezone
            if not user_timezone:
                zip_code = request.user.zip
                if not zip_code:
                    logger.warn('The user does not have a zip code associated so time zone cannot be retrieved.')
                    return

                location = geolocator.geocode(request.user.zip)
                if not location:
                    logger.error('Could not determine the user\'s location for zip code: %s.' % (str(zip_code)))
                    return

                user_timezone = location.raw.get('annotations', {}).get('timezone', {}).get('name', None)
                if not user_timezone:
                    logger.error('Could not determine the user\'s time zone.')
                    return

                if user_timezone:
                    request.user.timezone = user_timezone
                    request.user.save()

            try:
                timezone.activate(user_timezone)
            except Exception as e:
                logger.error('Invalid timezone selected: {0}'.format(e))
