# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0033_auto_20180718_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='val_model_id',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
