# -*- coding: utf-8 -*-
import requests

from celery.utils.log import get_task_logger
from django.conf import settings

from sitterfied.celeryapp import app
from sitterfied.users.models import User

logger = get_task_logger(__name__)


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
        logger.warning('Cannot retrieve time zone without a zip.')
        return

    logger.info('Retrieving time zone for {} using zip code {}.'.format(user.get_full_name(), zip_code))
    request_url = 'http://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees'.format(
        api_key=settings.ZIP_CODE_API_KEY,
        zip_code=zip_code
    )
    response = requests.get(request_url)
    if response.status_code != 200:
        logger.warning('No time zone found.')
        return

    time_zone = response.json().get('timezone').get('timezone_identifier')
    logger.info('Setting {}\'s time zone to {}.'.format(user.get_full_name(), time_zone))
    user.timezone = time_zone
    user.save()
