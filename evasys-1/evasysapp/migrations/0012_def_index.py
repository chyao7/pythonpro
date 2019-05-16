# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0011_auto_20180118_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='def_index',
            fields=[
                ('def_index_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('period', models.CharField(max_length=30, null=True)),
                ('evaluator', models.CharField(max_length=30, null=True)),
                ('def_junior_index', models.CharField(max_length=30, null=True)),
                ('def_senior_index', models.CharField(max_length=30, null=True)),
                ('memo', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
