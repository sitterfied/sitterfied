# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150129_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time_zone',
            field=models.CharField(default=b'America/New_York', max_length=255),
            preserve_default=True,
        ),
    ]
