# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sitterfied.db.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_sitterteammembership_source'),
    ]

    operations = [
        migrations.RunSQL(
            'alter table app_user drop constraint if exists app_user_email_6e5cff0ca7da609b_uniq;',
            'alter table app_user add constraint app_user_email_6e5cff0ca7da609b_uniq unique (email);',
            hints={'ignore': True},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=sitterfied.db.fields.CaseInsensitiveEmailField(unique=True, max_length=254, verbose_name=b'email address', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=sitterfied.db.fields.CaseInsensitiveCharField(unique=False, max_length=30, verbose_name=b'first name', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=sitterfied.db.fields.CaseInsensitiveCharField(unique=False, max_length=30, verbose_name=b'last name', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=sitterfied.db.fields.CaseInsensitiveCharField(error_messages={b'unique': b'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', b'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], help_text=b'Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name=b'username'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([]),
        ),
        migrations.RunSQL(
            'alter table app_user add constraint app_user_email_key unique (email);',
            'alter table app_user drop constraint if exists app_user_email_key;',
            hints={'ignore': True}
        ),
    ]
