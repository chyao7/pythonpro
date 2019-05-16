# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0067_auto_20190329_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='val_res',
            old_name='ind_model_cat',
            new_name='ind_model_cat_id',
        ),
    ]
