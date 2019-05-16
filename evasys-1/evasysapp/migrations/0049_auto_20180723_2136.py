# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0048_auto_20180723_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='evaluator_plot',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='period_plot',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='senior_plot',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
