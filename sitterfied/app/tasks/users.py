# -*- coding: utf-8 -*-
from celery.utils.log import get_task_logger
from django.conf import settings
from geopy import exc as geopy_exc, geocoders

from sitterfied.celeryapp import app
from sitterfied.users.models import User


logger = get_task_logger(__name__)
geolocator = geocoders.OpenCage(settings.OPEN_CAGE_API_KEY)


@app.task(bind=True)
def geocode_user(self, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return

    if user.timezone:
        return

    zip_code = user.zip
    if not zip_code:
        logger.warning('Cannot geocode without a zip.')
        return

    logger.info('Geocoding {} using zip code {}.'.format(user.get_full_name(), zip_code))
    try:
        location = geolocator.geocode(zip_code)
        if not location:
            raise geopy_exc.GeopyError('No location retrieved.')
    except geopy_exc.GeopyError as exc:
        raise self.retry(exc=exc)

    timezone = location.raw.get('annotations', {}).get('timezone', {}).get('name', None)
    if not timezone:
        logger.warning('Location retrieved, but no time zone found.')
        return

    logger.info('Setting {}\'s time zone to {}.'.format(user.get_full_name(), timezone))
    user.timezone = timezone
    user.save()
