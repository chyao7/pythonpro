# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0040_auto_20180720_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='val_res_id',
            field=models.CharField(primary_key=True, max_length=50, serialize=False),
        ),
    ]
