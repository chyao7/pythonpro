# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0038_auto_20180720_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_feedback',
            name='evaluation_content',
            field=models.TextField(max_length=400),
        ),
    ]
