# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0029_ind_model_ind_model_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_res',
            name='e_res',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='val_res',
            name='junior_res',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='val_res',
            name='p_index_res',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='val_res',
            name='p_res',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='evaluator_res',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='final_res',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='period_res',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='senior_res',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
