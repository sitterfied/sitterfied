# -*- coding: utf-8 -*-
import re

from datetime import datetime, timedelta

import app.signals as signals
import app.sms as sms
import app.utils as utils
import mock

from app.models import Booking, Parent, Sitter
from django.template.loader import render_to_string
from hamcrest import *

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
 
