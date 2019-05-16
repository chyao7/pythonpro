# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0059_auto_20180724_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='evaluator_plot',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='period_plot',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='senior_detail_plot',
            field=models.TextField(null=True),
        ),
    ]
