# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0019_algorithm_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(max_length=10, default=0, choices=[(0, '注册'), (1, '找回密码')]),
        ),
    ]
