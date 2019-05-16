# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0034_auto_20180718_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm_description',
            name='algorithm_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
