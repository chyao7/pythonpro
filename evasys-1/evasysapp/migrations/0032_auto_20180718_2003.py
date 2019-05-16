# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0031_auto_20180718_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='def_index',
            name='memo',
            field=models.CharField(max_length=30, default=None),
        ),
    ]
