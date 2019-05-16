# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0021_auto_20180630_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_feedback',
            fields=[
                ('feedback_id', models.CharField(primary_key=True, max_length=8, serialize=False)),
                ('evaluation_content', models.TextField()),
                ('feedback_content', models.TextField()),
                ('ctime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='company_id',
        ),
        migrations.AddField(
            model_name='ind_model',
            name='company_id',
            field=models.ForeignKey(null=True, to='evasysapp.company'),
        ),
        migrations.AddField(
            model_name='users',
            name='aff_company_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='val_model',
            name='company_id',
            field=models.ForeignKey(null=True, to='evasysapp.company'),
        ),
        migrations.AddField(
            model_name='val_res',
            name='algorithm_id',
            field=models.ForeignKey(null=True, to='evasysapp.Algorithm_description'),
        ),
        migrations.AddField(
            model_name='val_res',
            name='company_id',
            field=models.ForeignKey(null=True, to='evasysapp.company'),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='user_name',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='vcode',
            field=models.CharField(max_length=18),
        ),
        migrations.AddField(
            model_name='user_feedback',
            name='user_id',
            field=models.ForeignKey(to='evasysapp.users'),
        ),
    ]
