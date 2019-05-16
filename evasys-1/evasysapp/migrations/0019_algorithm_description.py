# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0018_auto_20180630_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm_description',
            fields=[
                ('algorithm_id', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('algorithm_name', models.CharField(max_length=100)),
                ('algorithm_img', models.ImageField(upload_to='')),
                ('algorithm_text', models.CharField(max_length=10000)),
            ],
        ),
    ]
