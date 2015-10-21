# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20150714_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitterteammembership',
            name='source',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
