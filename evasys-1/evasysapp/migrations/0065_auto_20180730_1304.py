# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0064_val_res_interval_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='val_res',
            name='interval_id',
        ),
        migrations.AddField(
            model_name='val_model',
            name='interval_id',
            field=models.ForeignKey(null=True, to='evasysapp.interval'),
        ),
    ]
