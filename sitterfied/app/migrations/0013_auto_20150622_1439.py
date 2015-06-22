# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_user_timezone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='cell',
            new_name='old_cell',
        ),
        migrations.AddField(
            model_name='parent',
            name='cell',
            field=models.CharField(blank=True, max_length=17, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{10,15}$', message=b'Phone number must be entered in the format: "+9999999999". Up to 15 digits allowed.')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sitter',
            name='cell',
            field=models.CharField(blank=True, max_length=17, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{10,15}$', message=b'Phone number must be entered in the format: "+9999999999". Up to 15 digits allowed.')]),
            preserve_default=True,
        ),
    ]
