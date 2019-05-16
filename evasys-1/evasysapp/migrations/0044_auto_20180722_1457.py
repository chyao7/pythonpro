# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0043_auto_20180722_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_model',
            name='company_name',
            field=models.ForeignKey(null=True, related_name='name_val', to='evasysapp.company', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='val_model',
            name='company_id',
            field=models.ForeignKey(null=True, related_name='id_val', to='evasysapp.company'),
        ),
    ]
