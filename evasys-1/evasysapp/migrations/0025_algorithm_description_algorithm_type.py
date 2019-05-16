# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0024_auto_20180702_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm_description',
            name='algorithm_type',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
