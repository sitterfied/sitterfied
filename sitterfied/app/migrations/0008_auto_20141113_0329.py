# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20141107_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingresponse',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingresponse',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingresponse',
            name='responded_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingresponse',
            name='response',
            field=models.CharField(default=b'pending', max_length=10, choices=[(b'accepted', b'accepted'), (b'active', b'active'), (b'canceled', b'canceled'), (b'completed', b'completed'), (b'declined', b'declined'), (b'expired', b'expired'), (b'pending', b'pending')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookingresponse',
            name='booking',
            field=models.ForeignKey(related_name=b'responses', to='app.Booking'),
        ),
        migrations.AlterField(
            model_name='bookingresponse',
            name='sitter',
            field=models.ForeignKey(related_name=b'responses', to='app.Sitter'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='sitter_teams',
            field=models.ManyToManyField(related_name=b'sitter_teams', through='app.SitterTeamMembership', to=b'app.Sitter', blank=True),
        ),
    ]
