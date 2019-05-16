# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evasysapp', '0020_emailverifyrecord_send_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverifyrecord',
            name='id',
        ),
        migrations.RemoveField(
            model_name='emailverifyrecord',
            name='user_id',
        ),
        migrations.AddField(
            model_name='emailverifyrecord',
            name='user_name',
            field=models.CharField(max_length=6, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='emailverifyrecord',
            name='vcode_id',
            field=models.CharField(primary_key=True, max_length=5, default=0, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='email',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(max_length=10, default=0, choices=[(0, '注册'), (1, '找回密码'), (2, '修改邮箱')]),
        ),
    ]
