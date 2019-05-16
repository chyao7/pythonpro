# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-27 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ind_model',
            fields=[
                ('ind_model_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ind_model_name', models.CharField(max_length=20, null=True)),
                ('ind_model_num', models.CharField(max_length=2)),
                ('ind_model_type', models.CharField(max_length=20)),
                ('data', models.CharField(max_length=10000)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='val_model',
            fields=[
                ('val_model_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('val_model_name', models.CharField(max_length=30)),
                ('data', models.CharField(max_length=10000)),
                ('ctime', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='val_res',
            fields=[
                ('val_model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='evasysapp.val_model', unique=True)),
                ('final_res', models.CharField(max_length=2)),
                ('period_res', models.CharField(max_length=10000)),
                ('evaluator_res', models.CharField(max_length=10000)),
                ('ctime', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='val_model',
            name='ind_model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.ind_model'),
        ),
        migrations.AddField(
            model_name='val_model',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users'),
        ),
    ]
