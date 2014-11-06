# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141106_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='dob',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='dob',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
