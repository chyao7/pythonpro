# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0036_auto_20180720_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_feedback',
            name='feedback_content',
        ),
    ]
