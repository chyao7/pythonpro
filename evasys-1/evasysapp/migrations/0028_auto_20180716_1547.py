# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0027_auto_20180716_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_model',
            name='datetype',
            field=models.IntegerField(null=True, choices=[(0, '年份'), (1, '季度'), (2, '月份')]),
        ),
    ]
