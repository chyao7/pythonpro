# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0025_algorithm_description_algorithm_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='aff_company_id',
        ),
        migrations.AddField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(null=True, to='evasysapp.users'),
        ),
    ]
