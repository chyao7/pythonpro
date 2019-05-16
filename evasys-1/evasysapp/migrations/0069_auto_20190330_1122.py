# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0068_auto_20190329_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_model',
            name='val_model_id',
            field=models.CharField(primary_key=True, max_length=50, serialize=False),
        ),
    ]
