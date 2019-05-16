# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0062_auto_20180724_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interval',
            name='interval_1',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='interval_2',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='interval_3',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='interval_4',
        ),
        migrations.RemoveField(
            model_name='interval',
            name='interval_5',
        ),
        migrations.AddField(
            model_name='interval',
            name='interval_data',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
