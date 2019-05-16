# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0045_auto_20180722_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ind_model',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='val_model',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='company_name',
        ),
    ]
