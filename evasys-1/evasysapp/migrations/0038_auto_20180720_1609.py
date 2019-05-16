# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0037_remove_user_feedback_feedback_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_feedback',
            name='feedback_id',
            field=models.CharField(primary_key=True, max_length=32, serialize=False),
        ),
    ]
