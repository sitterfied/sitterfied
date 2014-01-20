# -*- coding: utf-8 -*-
import logging

from django.utils import timezone
from geopy import geocoders
from tzwhere.tzwhere import tzwhere

__all__ = [
    'TimezoneMiddleware'
]

logger = logging.getLogger('app.middleware')

class TimezoneMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated():
            user_timezone = request.user.timezone
            if not user_timezone:
                zip_code = request.user.zip

                try:
                    place, (lat, lng) = geocoders.GoogleV3().geocode(zip_code)
                except Exception as e:
                    logger.error('Could not determine the user\'s location: %s' % (str(e)))
                    return

                try:
                    user_timezone = tzwhere().tzNameAt(lat, lng)
                except Exception as e:
                    logger.error('Could not determine the user\'s location: %s' % (str(e)))
                    return

                if not user_timezone:
                    logger.warn('Cannot set timezone for this user.')
                    return

                try:
                    request.user.timezone = user_timezone
                    request.user.save()
                except Exception as e:
                    logger.error('Could not save user\'s timezone: %s' % (str(e)))

            try:
                timezone.activate(user_timezone)
            except Exception as e:
                request.user.timezone = None
                logger.error('Invalid timezone selected: %s' % (str(e)))
