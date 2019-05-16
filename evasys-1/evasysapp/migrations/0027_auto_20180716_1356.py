# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0026_auto_20180713_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_model',
            name='datatime',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='val_model',
            name='datetype',
            field=models.IntegerField(default=0, choices=[(0, '年份'), (1, '季度'), (2, '月份')]),
        ),
    ]
