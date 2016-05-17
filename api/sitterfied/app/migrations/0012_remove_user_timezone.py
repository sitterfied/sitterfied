# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_booking_time_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='timezone',
        ),
    ]
