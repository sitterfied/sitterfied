# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20151101_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook_id',
            field=models.BigIntegerField(unique=True, null=True, blank=True),
        ),
    ]
