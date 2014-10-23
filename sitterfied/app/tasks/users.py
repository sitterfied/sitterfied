# -*- coding: utf-8 -*-
import time

import requests
from celery.utils.log import get_task_logger
from geopy import geocoders

from sitterfied.app.models import User
from sitterfied.celeryapp import app


logger = get_task_logger(__name__)


@app.task
def geocode_user(id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return None

    zip_code = user.zip
    if not zip_code:
        logger.info('Cannot geocode without a zip.')
        return None

    logger.info('Geocoding based on zip {0}'.format(zip_code))
    place, (lat, lng) = geocoders.GoogleV3().geocode(zip_code)
    return (lat, lng)


@app.task
def lookup_time_zone(latitude_and_longitude, id):
    if not id or not latitude_and_longitude:
        return None

    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return None

    if user.timezone:
        return None

    latitude, longitude = latitude_and_longitude
    logger.info('Looking up timezone for {0}, {1}'.format(latitude, longitude))
    r = requests.get('https://maps.googleapis.com/maps/api/timezone/json?location={0},{1}&timestamp={2}&sensor=false'
                     .format(latitude, longitude, int(time.time())))
    json = r.json()
    try:
        user.timezone = json.get('timeZoneId')
        user.save()
    except Exception:
        return None

    return user.timezone
