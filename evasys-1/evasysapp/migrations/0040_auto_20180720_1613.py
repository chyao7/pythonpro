# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0039_auto_20180720_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_feedback',
            name='evaluation_content',
            field=models.TextField(),
        ),
    ]
