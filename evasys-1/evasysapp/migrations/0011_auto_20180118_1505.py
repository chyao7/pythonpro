# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0010_auto_20180117_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='def_index',
            name='evaluator_id',
        ),
        migrations.RemoveField(
            model_name='def_index',
            name='period_id',
        ),
        migrations.RemoveField(
            model_name='def_index',
            name='senior_index_id',
        ),
        migrations.DeleteModel(
            name='def_evaluator',
        ),
        migrations.DeleteModel(
            name='def_index',
        ),
        migrations.DeleteModel(
            name='def_period',
        ),
        migrations.DeleteModel(
            name='def_senior_index',
        ),
    ]
