# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0032_auto_20180718_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='e_res',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='final_res',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='p_res',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
