# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0063_auto_20180730_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_res',
            name='interval_id',
            field=models.ForeignKey(null=True, to='evasysapp.interval'),
        ),
    ]
