# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0017_delete_def_senior_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vcode', models.CharField(max_length=8)),
                ('send_time', models.DateTimeField(null=True, auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='mobilphone',
            field=models.IntegerField(unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='emailverifyrecord',
            name='email',
            field=models.ForeignKey(related_name='email_record', to='evasysapp.users', to_field='email'),
        ),
        migrations.AddField(
            model_name='emailverifyrecord',
            name='user_id',
            field=models.ForeignKey(related_name='user_record', to='evasysapp.users'),
        ),
    ]
