# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0015_def_index_senior_index_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='def_index',
            name='senior_index_id',
        ),
    ]
