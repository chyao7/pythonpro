# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0050_auto_20180723_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='val_model_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
