# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20160128_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitterteammembership',
            name='source',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
