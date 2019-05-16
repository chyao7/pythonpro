# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0054_auto_20180723_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='val_res',
            name='evaluator_plot',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='period_plot',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='senior_plot',
        ),
    ]
