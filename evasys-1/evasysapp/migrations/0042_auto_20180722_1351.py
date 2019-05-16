# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0041_auto_20180722_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ind_model',
            name='user_id',
            field=models.ForeignKey(null=True, to='evasysapp.users'),
        ),
    ]
