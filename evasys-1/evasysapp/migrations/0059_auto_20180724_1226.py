# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0058_auto_20180723_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='val_res',
            old_name='senior_plot',
            new_name='senior_detail_plot',
        ),
    ]
