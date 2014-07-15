# -*- coding: utf-8 -*-
from datetime import datetime

import pytz
from celery.utils.log import get_task_logger
from django.template.loader import render_to_string
from django.utils import timezone

from app.models import Reminder
from app.sms import send_message
from app.utils import get_short_url
from sitterfied.celeryapp import app


logger = get_task_logger(__name__)


seconds_in_hour = 3600


@app.task
def send_reminders(id, seconds, reminders):
    reminder = Reminder.objects.get(pk=id)
    booking = reminder.booking
    parent = booking.parent
    sitter = booking.accepted_sitter

    tz = pytz.timezone(parent.timezone) if parent.timezone else pytz.UTC
    start_date_time = tz.normalize(booking.start_date_time)
    stop_date_time = tz.normalize(booking.stop_date_time)

    if parent.settings.mobile_booking_accepted_denied and parent.cell:
        send_parent_reminder(parent, sitter, start_date_time, stop_date_time, seconds, tz)

    if sitter.settings.mobile_booking_accepted_denied and sitter.cell:
        send_sitter_reminder(sitter, parent, start_date_time, stop_date_time, seconds, tz)

    if reminders:
        queue_next_reminder(reminder, reminders)


def queue_next_reminder(reminder, reminders):
    next_reminder = reminders.pop(0)
    next_eta = datetime.strptime(next_reminder['eta'], '%Y-%m-%d %H:%M:%S')
    next_seconds = next_reminder['seconds']

    result = send_reminders.apply_async(
        eta=pytz.UTC.localize(next_eta),
        kwargs={
            'id': reminder.id,
            'seconds': next_seconds,
            'reminders': reminders,
        }
    )
    reminder.task_id = result.task_id
    reminder.save()


def send_parent_reminder(parent, sitter, start_date_time, stop_date_time, seconds, tz):
    try:
        timezone.activate(tz)

        if seconds:
            if seconds == 180:
                hours = 24
            elif seconds == 60:
                hours = 1
            else:
                hours = seconds / seconds_in_hour

            template = 'sms/reminder/parent/{0}_hour_reminder.sms'.format(hours)
            sms = render_to_string(template, {
                'sitter_full_name': sitter.get_full_name(),
                'sitter_first_name': sitter.first_name,
                'sitter_cell': sitter.cell,
                'hours': hours,
                'start_date_time': start_date_time.replace(),
                'stop_date_time': stop_date_time.replace(),
                'short_url': get_short_url('/mybookings/upcoming'),
            })
        else:
            template = 'sms/reminder/parent/relieve_sitter_reminder.sms'
            sms = render_to_string(template, {
                'sitter_first_name': sitter.first_name,
                'sitter_cell': sitter.cell,
                'stop_date_time': stop_date_time.replace(),
            })

            send_message(sms, parent.cell)
    except Exception as ex:
        raise ex
    finally:
        timezone.deactivate()


def send_sitter_reminder(sitter, parent, start_date_time, stop_date_time, seconds, tz):
    try:
        timezone.activate(tz)

        if seconds:
            if seconds == 180:
                hours = 24
            elif seconds == 60:
                hours = 1
            else:
                hours = seconds / seconds_in_hour

            template = 'sms/reminder/sitter/{0}_hour_reminder.sms'.format(hours)
            sms = render_to_string(template, {
                'parent_full_name': parent.get_full_name(),
                'parent_first_name': parent.first_name,
                'parent_cell': parent.cell,
                'hours': hours,
                'start_date_time': start_date_time.replace(),
                'stop_date_time': stop_date_time.replace(),
                'short_url': get_short_url('/mybookings/upcoming'),
            })

            send_message(sms, sitter.cell)
    except Exception as ex:
        raise ex
    finally:
        timezone.deactivate()
