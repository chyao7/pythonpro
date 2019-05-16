# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0030_auto_20180718_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_model',
            name='ind_model_cat',
            field=models.ForeignKey(null=True, related_name='cat_val', to='evasysapp.ind_model', to_field='ind_model_cat'),
        ),
        migrations.AddField(
            model_name='val_res',
            name='ind_model_cat',
            field=models.ForeignKey(null=True, related_name='cat_res', to='evasysapp.ind_model', to_field='ind_model_cat'),
        ),
        migrations.AlterField(
            model_name='val_model',
            name='ind_model_id',
            field=models.ForeignKey(related_name='ind_val', to='evasysapp.ind_model'),
        ),
    ]
