# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0069_auto_20190330_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='val_model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='evasysapp.val_model'),
        ),
    ]
