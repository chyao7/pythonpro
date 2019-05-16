# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0042_auto_20180722_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='ind_model',
            name='company_name',
            field=models.ForeignKey(null=True, related_name='name_ind', to='evasysapp.company', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='ind_model',
            name='company_id',
            field=models.ForeignKey(null=True, related_name='id_ind', to='evasysapp.company'),
        ),
    ]
