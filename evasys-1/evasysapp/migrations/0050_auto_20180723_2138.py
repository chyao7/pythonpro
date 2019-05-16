# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0049_auto_20180723_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='junior_res',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='p_index_res',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='senior_res',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
