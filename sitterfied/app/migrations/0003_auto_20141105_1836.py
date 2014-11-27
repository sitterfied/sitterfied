# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141104_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='user',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(default=b'active', max_length=10, choices=[(b'accepted', b'accepted'), (b'active', b'active'), (b'canceled', b'canceled'), (b'completed', b'completed'), (b'declined', b'declined'), (b'expired', b'expired'), (b'pending', b'pending')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_type',
            field=models.CharField(default=b'job', max_length=20, choices=[(b'interview', b'interview'), (b'job', b'job'), (b'meetup', b'meetup'), (b'phone', b'phone')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='state',
            field=models.CharField(default=b'NJ', max_length=2, blank=True, choices=[(b'AL', b'AL'), (b'AK', b'AK'), (b'AZ', b'AZ'), (b'AR', b'AR'), (b'CA', b'CA'), (b'CO', b'CO'), (b'CT', b'CT'), (b'DE', b'DE'), (b'DC', b'DC'), (b'FL', b'FL'), (b'GA', b'GA'), (b'HI', b'HI'), (b'ID', b'ID'), (b'IL', b'IL'), (b'IN', b'IN'), (b'IA', b'IA'), (b'KS', b'KS'), (b'KY', b'KY'), (b'LA', b'LA'), (b'ME', b'ME'), (b'MD', b'MD'), (b'MA', b'MA'), (b'MI', b'MI'), (b'MN', b'MN'), (b'MS', b'MS'), (b'MO', b'MO'), (b'MT', b'MT'), (b'NE', b'NE'), (b'NV', b'NV'), (b'NH', b'NH'), (b'NJ', b'NJ'), (b'NM', b'NM'), (b'NY', b'NY'), (b'NC', b'NC'), (b'ND', b'ND'), (b'OH', b'OH'), (b'OK', b'OK'), (b'OR', b'OR'), (b'PA', b'PA'), (b'RI', b'RI'), (b'SC', b'SC'), (b'SD', b'SD'), (b'TN', b'TN'), (b'TX', b'TX'), (b'UT', b'UT'), (b'VT', b'VT'), (b'VA', b'VA'), (b'WA', b'WA'), (b'WV', b'WV'), (b'WI', b'WI'), (b'WY', b'WY')]),
        ),
        migrations.AlterField(
            model_name='settings',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(default=b'trial', max_length=10, choices=[(b'paid', b'paid'), (b'trial', b'trial')]),
        ),
    ]
