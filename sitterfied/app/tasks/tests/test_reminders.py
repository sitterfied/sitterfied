# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from django.db.models.signals import pre_save, m2m_changed, pre_delete
from pytz import timezone

from app import signals
from app.models import Booking, Parent, Reminder, Sitter
from app.tasks import reminders
from app.tasks.tests import utils


def test_send_reminders():
    try:
        disconnect_signals()

        booking = create_booking()
        booking.save()

        reminder = Reminder()
        reminder.booking = booking
        reminder.save()

        reminders.send_reminders(reminder.id, 24)
        reminders.send_reminders(reminder.id, 2)
    finally:
        try:
            booking.delete()
            reminder.delete()
        finally:
            reconnect_signals()


def create_booking():
    eastern = timezone('America/New_York')

    booking = Booking()
    booking.start_date_time = eastern.localize(datetime.now() + timedelta(days=1, minutes=5))
    booking.stop_date_time = booking.start_date_time + timedelta(hours=3)
    booking.parent = Parent.objects.get(first_name='Parent')
    booking.accepted_sitter = Sitter.objects.get(first_name='Sitter')
    return booking


def disconnect_signals():
    utils.disconnect_signal(m2m_changed, signals.receive_booking_request, Booking)
    utils.disconnect_signal(pre_save, signals.reminder_save_handler, Reminder)
    utils.disconnect_signal(pre_delete, signals.reminder_del_handler, Reminder)


def reconnect_signals():
    utils.reconnect_signal(m2m_changed, signals.receive_booking_request, Booking)
    utils.reconnect_signal(pre_save, signals.reminder_save_handler, Reminder)
    utils.reconnect_signal(pre_delete, signals.reminder_del_handler, Reminder)
