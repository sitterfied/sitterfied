# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141106_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='dob',
            field=models.DateField(),
        ),
    ]
