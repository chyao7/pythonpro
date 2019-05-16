# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='val_res',
            name='algorithm_id',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='e_res',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='evaluator_res',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='junior_res',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='p_index_res',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='p_res',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='period_res',
        ),
        migrations.RemoveField(
            model_name='val_res',
            name='senior_res',
        ),
        migrations.AddField(
            model_name='val_res',
            name='first_ind_res',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='val_res',
            name='second_ind_res',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='final_res',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
