# -*- coding: utf-8 -*-
import logging

from django.utils import timezone

from sitterfied.app.tasks import users

__all__ = [
    'TimezoneMiddleware'
]

logger = logging.getLogger('app.middleware')


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

                users.geocode_user.s(request.user.id).delay()

            try:
                if user_timezone:
                    timezone.activate(user_timezone)
            except Exception as e:
                logger.error('Invalid timezone selected: {0}'.format(e))
