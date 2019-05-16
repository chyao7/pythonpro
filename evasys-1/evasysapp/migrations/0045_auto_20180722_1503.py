# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0044_auto_20180722_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='val_res',
            name='company_name',
            field=models.ForeignKey(null=True, related_name='name_res', to='evasysapp.company', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='val_res',
            name='company_id',
            field=models.ForeignKey(null=True, related_name='id_res', to='evasysapp.company'),
        ),
    ]
