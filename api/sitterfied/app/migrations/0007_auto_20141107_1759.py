# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20141107_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_type',
            field=models.CharField(default=b'job', max_length=20, choices=[(b'job', b'job'), (b'meetup', b'meetup'), (b'phone', b'phone')]),
        ),
    ]
