# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitterfied.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20151023_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=sitterfied.db.fields.CaseInsensitiveCharField(unique=True, max_length=128),
        ),
    ]
