# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0006_auto_20180104_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_res',
            name='val_model_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.val_model'),
            preserve_default=False,
        ),
    ]
