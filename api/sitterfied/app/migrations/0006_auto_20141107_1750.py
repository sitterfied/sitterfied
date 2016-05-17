# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def convert_booking_status(apps, schema_editor):
    # We can't import the Booking model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Booking = apps.get_model('app', 'Booking')
    for booking in Booking.objects.all():
        booking.booking_status = booking.booking_status.lower()
        booking.save()


def convert_booking_type(apps, schema_editor):
    Booking = apps.get_model('app', 'Booking')
    for booking in Booking.objects.all():
        booking_type = booking.booking_type.upper()
        if booking_type == 'JOB':
            booking_type = 'job'
        elif booking_type == 'PHONE INTERVIEW':
            booking_type = 'phone'
        elif booking_type == 'MEETUP INTERVIEW':
            booking_type = 'meetup'

        if booking.booking_type.upper() != booking_type:
            booking.booking_type = booking_type
            booking.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20141107_1718'),
    ]

    operations = [
        migrations.RunPython(convert_booking_status),
        migrations.RunPython(convert_booking_type),
    ]
