# -*- coding: utf-8 -*-
import logging
import math
from datetime import datetime

import pytz
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone

from sitterfied.app.sms import send_message
from sitterfied.app.utils import get_short_url
from sitterfied.bookings.models import Reminder
from sitterfied.celeryapp import app
from sitterfied.utils import time
from sitterfied.utils.tasks import get_eta, reschedule

logger = logging.getLogger(__name__)
seconds_in_hour = 3600


def calculate_eta(timestamp, delta):
    if getattr(settings, 'FAST_SEND_REMINDERS', False):
        return time.now() + delta
    else:
        return timestamp - delta


def get_time_delta(seconds):
    seconds_in_minute = 60
    seconds_in_hour = 3600

    if seconds >= seconds_in_hour:
        hours = seconds / seconds_in_hour
        if hours >= 48:
            return 'in ' + ('%g' % round(math.ceil(hours / 24), 2)) + ' days'
        elif hours >= 24:
            return 'tomorrow'
        else:
            return 'in ' + str(hours) + ' ' + ('hours' if hours > 1 else 'hour')
    else:
        minutes = seconds / seconds_in_minute
        return 'in ' + str(minutes) + ' ' + ('minutes' if minutes > 1 else 'minute')


@app.task(acks_late=True)
def send_reminders(id, reminder_type, seconds, reminders, *args, **kwargs):
    logger.info('Send reminders task starting...')
    reminder = Reminder.objects.get(pk=id)
    booking = reminder.booking
    parent = booking.parent
    sitter = booking.accepted_sitter

    tz = pytz.timezone(parent.timezone) if parent.timezone else pytz.UTC
    start_date_time = tz.normalize(booking.start_date_time)
    stop_date_time = tz.normalize(booking.stop_date_time)

    if parent.settings.mobile_booking_accepted_denied and parent.cell:
        send_parent_reminder(parent, sitter, start_date_time, stop_date_time, reminder_type, seconds, tz)

    if sitter.settings.mobile_booking_accepted_denied and sitter.cell:
        send_sitter_reminder(sitter, parent, start_date_time, stop_date_time, reminder_type, seconds, tz)

    if reminders:
        queue_next_reminder(reminder, reminders)


def queue_next_reminder(reminder, reminders):
    next_reminder = reminders.pop(0)
    next_eta = datetime.strptime(next_reminder['eta'], '%Y-%m-%d %H:%M:%S')
    next_reminder_type = next_reminder['reminder_type']
    next_seconds = next_reminder['seconds']

    result = send_reminders.apply_async(
        eta=get_eta(pytz.UTC.localize(next_eta)),
        kwargs={
            'desired_eta': pytz.UTC.localize(next_eta).strftime('%Y-%m-%d %H:%M:%S'),
            'id': reminder.id,
            'reminder_type': next_reminder_type,
            'seconds': next_seconds,
            'reminders': reminders,
        }
    )
    reminder.task_id = result.task_id
    reminder.save()


def send_parent_reminder(parent, sitter, start_date_time, stop_date_time, reminder_type, seconds, tz):
    try:
        timezone.activate(tz)

        if reminder_type in ['first', 'second']:
            template = 'sms/reminder/parent/{0}_reminder.sms'.format(reminder_type)
            sms = render_to_string(template, {
                'sitter_full_name': sitter.get_full_name(),
                'sitter_first_name': sitter.first_name,
                'sitter_cell': sitter.cell,
                'timedelta': get_time_delta(seconds),
                'start_date_time': start_date_time.replace(),
                'stop_date_time': stop_date_time.replace(),
                'short_url': get_short_url('/mybookings/upcoming'),
            })
        else:
            template = 'sms/reminder/parent/relieve_sitter_reminder.sms'
            sms = render_to_string(template, {
                'sitter_first_name': sitter.first_name,
                'sitter_cell': sitter.cell,
                'timedelta': get_time_delta(seconds),
                'stop_date_time': stop_date_time.replace(),
            })

        send_message(sms, parent.cell)
    except Exception as ex:
        raise ex
    finally:
        timezone.deactivate()


def send_sitter_reminder(sitter, parent, start_date_time, stop_date_time, reminder_type, seconds, tz):
    try:
        timezone.activate(tz)

        if reminder_type in ['first', 'second']:
            template = 'sms/reminder/sitter/{0}_reminder.sms'.format(reminder_type)
            sms = render_to_string(template, {
                'parent_full_name': parent.get_full_name(),
                'parent_first_name': parent.first_name,
                'parent_cell': parent.cell,
                'timedelta': get_time_delta(seconds),
                'start_date_time': start_date_time.replace(),
                'stop_date_time': stop_date_time.replace(),
                'short_url': get_short_url('/mybookings/upcoming'),
            })

            send_message(sms, sitter.cell)
    except Exception as ex:
        raise ex
    finally:
        timezone.deactivate()
