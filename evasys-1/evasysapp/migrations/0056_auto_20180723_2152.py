# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0055_auto_20180723_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ind_model',
            name='data',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='val_model',
            name='data',
            field=models.TextField(max_length=10000),
        ),
    ]
