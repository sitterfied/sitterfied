# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta

import mock
import pytz
from django.template.loader import render_to_string
from hamcrest import *
from pytz import timezone

from app import signals, sms, utils
from app.models import Booking, Parent, Sitter, Reminder


def test_booking_request_message():
    sitter = Sitter()
    sitter.first_name = 'Devon'
    sitter.cell = '+17322397588'

    parent = Parent()
    parent.full_name = 'Elana Nanscawen'

    instance = Booking()
    instance.id = 22
    instance.start_date_time = datetime.now()
    instance.stop_date_time = instance.start_date_time + timedelta(hours=5)

    short_url = 'test.sttrfd.us/' + utils.generate_short_url_code()

    message = render_to_string("sms/booking/booking_request_received.sms", {
        'sitter_name': sitter.first_name,
        'parent_name': parent.full_name,
        'start_date_time': instance.start_date_time,
        'stop_date_time': instance.stop_date_time,
        'short_url': short_url,
        'booking_code': instance.id,
        'num_sitters': str(len(instance.sitters.all()))
    })

    assert_that(message, string_contains_in_order(
        sitter.first_name,
        parent.full_name,
        re.sub('^0', '', instance.start_date_time.strftime('%b %d')),
        re.sub('^0', '', instance.start_date_time.strftime('%I:%M%p').lower()),
        re.sub('^0', '', instance.stop_date_time.strftime('%I:%M%p').lower()),
        short_url,
        str(instance.id),
        str(instance.id),
    ))

    message = render_to_string('sms/booking/booking_request_received_multiple.sms', {
        'sitter_name': sitter.first_name,
        'parent_name': parent.full_name,
        'start_date_time': instance.start_date_time,
        'stop_date_time': instance.stop_date_time,
        'short_url': short_url,
        'booking_code': instance.id,
        'num_sitters': str(len(instance.sitters.all()))
    })

    assert_that(message, string_contains_in_order(
        sitter.first_name,
        parent.full_name,
        str(len(instance.sitters.all())),
        re.sub('^0', '', instance.start_date_time.strftime('%b %d')),
        re.sub('^0', '', instance.start_date_time.strftime('%I:%M%p').lower()),
        re.sub('^0', '', instance.stop_date_time.strftime('%I:%M%p').lower()),
        short_url,
        str(instance.id),
        str(instance.id),
    ))
    #sms.client.messages.create(body=message, to=sitter.cell,
    #from_=sms.sitterfied_number


def test_new_sitter_signal():
    sitter = mock.Mock(spec=Sitter)
    sitter.email = 'alewisohn@gmail.com'
    sitter.first_name = 'Test'
    sitter.last_name = 'Signals'
    
    signals.new_sitter(sitter, sitter, created=True)


def test_new_parent_signal():
    parent = mock.Mock(spec=Parent)
    parent.email = 'alewisohn@gmail.com'
    parent.first_name = 'Test'
    parent.last_name = 'Signals'
    
    signals.new_parent(parent, parent, created=True)


def test_reminder_save_handler():
    eastern = timezone('US/Eastern')

    booking = Booking()
    booking.start_date_time = datetime.now() + timedelta(days=1, minutes=5)
    booking.stop_date_time = booking.start_date_time + timedelta(hours=3)
    booking.parent = Parent()
    booking.accepted_sitter = Sitter()

    reminder = Reminder()
    reminder.booking = booking
    
    signals.reminder_save_handler(instance=reminder)
