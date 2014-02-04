# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import app.signals as signals
import app.sms as sms
import app.utils as utils

from app.models import Booking, Parent, Sitter
from django.template.loader import render_to_string

def test_receive_booking_request():
    sitter = Sitter()
    sitter.first_name = 'Dana'
    sitter.cell = '+17322397588'

    parent = Parent()
    parent.first_name = 'Elana'

    instance = Booking()
    instance.id = 22
    instance.start_date_time = datetime.now()
    instance.stop_date_time = instance.start_date_time + timedelta(hours=5)

    message = render_to_string("email/booking/booking_request_received.sms", {
        'sitter_name': sitter.first_name,
        'parent_name': parent.first_name,
        'start_date_time': instance.start_date_time,
        'stop_date_time': instance.stop_date_time,
        'short_url': 'test.sttrfd.us/' + utils.generate_short_url_code(),
        'booking_code': instance.id,
    })
    sms.client.messages.create(body=message, to=sitter.cell, from_=sms.sitterfied_number)
