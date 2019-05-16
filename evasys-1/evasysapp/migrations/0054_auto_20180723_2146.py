# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0053_auto_20180723_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='evaluator_plot',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='period_plot',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='senior_plot',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
