# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0016_remove_def_index_senior_index_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='def_senior_index',
        ),
    ]
