# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0005_val_res_senior_res'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='val_res',
            name='val_model_id',
        ),
        migrations.AddField(
            model_name='val_res',
            name='val_res_id',
            field=models.CharField(default=0, max_length=30, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
