# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def migrate_phone_numbers(apps, schema_editor):
    Parent = apps.get_model('app', 'Parent')
    Sitter = apps.get_model('app', 'Sitter')

    for parent in Parent.objects.filter(old_cell__isnull=False):
        try:
            parent.cell = parent.old_cell
            parent.save()
        except:
            pass

    for sitter in Sitter.objects.filter(old_cell__isnull=False):
        try:
            sitter.cell = parent.old_cell
            sitter.save()
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20150622_1439'),
    ]

    operations = [
        migrations.RunPython(migrate_phone_numbers)
    ]
