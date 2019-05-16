# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0047_auto_20180723_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='val_res',
            name='evaluator_plot',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
