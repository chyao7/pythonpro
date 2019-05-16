# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0065_auto_20180730_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='val_model_id',
            field=models.ForeignKey(default=datetime.datetime(2019, 3, 29, 19, 56, 0, 388782), to='evasysapp.val_model'),
            preserve_default=False,
        ),
    ]
