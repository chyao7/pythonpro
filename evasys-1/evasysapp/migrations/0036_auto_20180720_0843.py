# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0035_auto_20180720_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm_description',
            name='algorithm_text',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
