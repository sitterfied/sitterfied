# -*- coding: utf-8 -*-
import json
from datetime import datetime, timedelta

from django.db.models.signals import pre_save, m2m_changed, pre_delete
from django.template.loader import render_to_string
from hamcrest import *
from pytz import timezone

from sitterfied.app import signals
from sitterfied.app.models import Booking, Parent, Reminder, Sitter
from sitterfied.app.tasks import reminders
from sitterfied.app.tasks.tests import utils


def test_time_conversions():
    tz = timezone('America/New_York')
    eta = (datetime.now(tz) - timedelta(seconds=3600)).strftime("%Y-%m-%d %H:%M:%S")
    print eta
    print json.dumps(eta)
    pdate = datetime.strptime(eta, '%Y-%m-%d %H:%M:%S')
    print pdate
    print tz.localize(pdate)


def test_get_time_delta():
    # Hours
    assert_that(reminders.get_time_delta(1 * 3600), is_('in 1 hour'))
    assert_that(reminders.get_time_delta(18 * 3600), is_('in 18 hours'))
    assert_that(reminders.get_time_delta(24 * 3600), is_('tomorrow'))
    assert_that(reminders.get_time_delta(36 * 3600), is_('tomorrow'))
    assert_that(reminders.get_time_delta(48 * 3600), is_('in 2 days'))
    assert_that(reminders.get_time_delta(52 * 3600), is_('in 2 days'))
    assert_that(reminders.get_time_delta(72 * 3600), is_('in 3 days'))

    # Minutes
    assert_that(reminders.get_time_delta(24 * 60), is_('in 24 minutes'))
    assert_that(reminders.get_time_delta(1 * 60), is_('in 1 minute'))


def test_first_reminder_strings():
    now = datetime.utcnow()
    stop_time = now + timedelta(hours=1)
    cell = '+15555555555'
    first_name = 'Jane'
    name = 'Jane Doe'
    delta = reminders.get_time_delta(3600)
    sms = render_to_string('sms/reminder/parent/first_reminder.sms', {
        'sitter_full_name': name,
        'sitter_first_name': first_name,
        'sitter_cell': cell,
        'timedelta': delta,
        'start_date_time': now,
        'stop_date_time': stop_time,
        'short_url': '/mybookings/upcoming',
    })

    assert_that(sms, is_(u'{0} will be arriving {1}. {2}\'s # is: {3}. Go to {4} for details.\n'.format(
        name,
        delta,
        first_name,
        cell,
        '/mybookings/upcoming',
    )))


def test_relief_reminder_strings():
    now = datetime.utcnow()
    cell = '+15555555555'
    name = 'Jane'
    delta = reminders.get_time_delta(3600)
    sms = render_to_string('sms/reminder/parent/relieve_sitter_reminder.sms', {
        'sitter_first_name': name,
        'sitter_cell': cell,
        'timedelta': delta,
        'stop_date_time': now,
    })

    assert_that(sms, is_(u'Friendly reminder that you need to relieve {0} {3} ({2}). {0}\u2019s # is: {1}. Try not to be late :)\n'.format(
        name,
        cell,
        get_time_code(now),
        delta,
    )))


def get_time_code(instant):
    hour = instant.strftime('%I').lstrip('0')
    rest = instant.strftime(':%M%p').lower()
    return hour + rest


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
