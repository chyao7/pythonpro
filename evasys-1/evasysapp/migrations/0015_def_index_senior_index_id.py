# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0014_def_senior_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='def_index',
            name='senior_index_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
