# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0028_auto_20180716_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='ind_model',
            name='ind_model_cat',
            field=models.CharField(max_length=20, unique=True, null=True),
        ),
    ]
