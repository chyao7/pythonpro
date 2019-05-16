# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import evasysapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0046_auto_20180722_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_res',
            name='evaluator_plot',
            field=models.ImageField(null=True),
        ),
        migrations.AddField(
            model_name='val_res',
            name='period_plot',
            field=models.ImageField(null=True),
        ),
        migrations.AddField(
            model_name='val_res',
            name='senior_plot',
            field=models.ImageField(null=True),
        ),
    ]
