# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0066_auto_20190329_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='ind_model_cat',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
