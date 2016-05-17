# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone


def migrate_responses(apps, schema_editor):
    Booking = apps.get_model('app', 'Booking')
    BookingResponse = apps.get_model('app', 'BookingResponse')

    for booking in Booking.objects.all():
        responses = BookingResponse.objects.filter(booking=booking)

        for declined in booking.declined_sitters.all():
            response = responses.get(sitter=declined)
            response.response = 'declined'
            response.responded_at = timezone.now()
            response.save()

        responses.filter(
            sitter=booking.accepted_sitter
        ).update(
            response='accepted', responded_at=timezone.now())

        responses.update(created=booking.created)

    for booking in Booking.objects.filter(stop_date_time__lt=timezone.now()):
        status = 'canceled' if booking.canceled else 'expired'
        BookingResponse.objects.filter(
            booking=booking, response='pending'
        ).update(
            response=status, responded_at=timezone.now())


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20141113_0329'),
    ]

    operations = [
        migrations.RunPython(migrate_responses),
        migrations.RemoveField(
            model_name='booking',
            name='accepted_sitter',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='declined_sitters',
        ),
        migrations.AlterField(
            model_name='reminder',
            name='booking',
            field=models.ForeignKey(related_name=b'reminders', to='app.Booking'),
        ),
    ]
