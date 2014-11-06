# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141105_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitterteammembership',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sitterteammembership',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='sitterteammembership',
            unique_together=set([('parent', 'sitter')]),
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Settings', 'verbose_name_plural': 'Settings'},
        ),
        migrations.AlterField(
            model_name='parent',
            name='sitter_teams',
            field=models.ManyToManyField(related_name=b'parents', through='app.SitterTeamMembership', to=b'app.Sitter', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('email',)]),
        ),
    ]
