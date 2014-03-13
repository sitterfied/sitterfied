# -*- coding: utf-8 -*-
from datetime import timedelta

import pytz
from celery.utils.log import get_task_logger
from django.template.loader import render_to_string

from app.models import Reminder
from app.sms import send_message
from app.utils import get_short_url
from sitterfied.celeryapp import app


logger = get_task_logger(__name__)


@app.task
def send_reminders(id, hours):
    reminder = Reminder.objects.get(pk=id)
    booking = reminder.booking
    parent = booking.parent
    sitter = booking.accepted_sitter

    if parent.settings.mobile_booking_accepted_denied and parent.cell:
        template = 'sms/reminder/parent/{0}_hour_reminder.sms'.format(hours)
        sms = render_to_string(template, {
            'sitter_full_name': sitter.get_full_name(),
            'sitter_first_name': sitter.first_name,
            'sitter_cell': sitter.cell,
            'hours': hours,
            'start_date_time': booking.start_date_time,
            'stop_date_time': booking.stop_date_time,
            'short_url': get_short_url('/mybooking/upcoming'),
        })
        send_message(sms, parent.cell)

    if hours >= 2 and sitter.settings.mobile_booking_accepted_denied and sitter.cell:
        template = 'sms/reminder/sitter/{0}_hour_reminder.sms'.format(hours)
        sms = render_to_string(template, {
            'parent_full_name': parent.get_full_name(),
            'parent_first_name': parent.first_name,
            'parent_cell': parent.cell,
            'hours': hours,
            'start_date_time': booking.start_date_time,
            'stop_date_time': booking.stop_date_time,
            'short_url': get_short_url('/mybooking/upcoming'),
        })
        send_message(sms, sitter.cell)

    if hours == 24:
        eta = booking.start_date_time - timedelta(hours=2)
        result = send_reminders.apply_async(eta=eta.astimezone(pytz.UTC), kwargs={'id': reminder.id, 'hours': 2})
        reminder.task_id = result.task_id
        reminder.save()
    elif hours == 2:
        eta = booking.stop_date_time - timedelta(hours=1)
        result = send_reminders.apply_async(eta=eta.astimezone(pytz.UTC), kwargs={'id': reminder.id, 'hours': 1})
        reminder.task_id = result.task_id
        reminder.save()
