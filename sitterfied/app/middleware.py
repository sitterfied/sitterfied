# -*- coding: utf-8 -*-
import logging

from django.utils import timezone

from sitterfied.app.tasks import users as tasks

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
                if not zip_code:
                    logger.warn('The user does not have a zip code associated so time zone cannot be retrieved.')
                    return

                try:
                    (tasks.geocode_user.s(request.user.id) | tasks.lookup_time_zone.s(request.user.id)).delay()
                except Exception as e:
                    logger.error('Could not determine the user\'s location: %s' % (str(e)))
                    return

            try:
                timezone.activate(user_timezone)
            except Exception as e:
                logger.error('Invalid timezone selected: {0}'.format(e))
