# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-18 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm_description',
            fields=[
                ('algorithm_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('algorithm_name', models.CharField(max_length=100)),
                ('algorithm_type', models.CharField(max_length=4, null=True)),
                ('algorithm_img', models.ImageField(null=True, upload_to='')),
                ('algorithm_text', models.CharField(max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('company_id', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=40, unique=True)),
                ('liscom_code', models.CharField(default=0, max_length=6)),
                ('company_address', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('introduction', models.CharField(max_length=500)),
                ('website', models.CharField(max_length=100, null=True)),
                ('img_address', models.CharField(max_length=100, null=True)),
                ('intro_address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='def_index',
            fields=[
                ('junior_index_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('period_name', models.CharField(max_length=30, null=True)),
                ('evaluator_name', models.CharField(max_length=30, null=True)),
                ('junior_index_name', models.CharField(max_length=30, null=True)),
                ('senior_index_name', models.CharField(max_length=30, null=True)),
                ('memo', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('vcode_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=6, null=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('vcode', models.CharField(max_length=18)),
                ('send_type', models.CharField(choices=[(0, '注册'), (1, '找回密码'), (2, '修改邮箱')], default=0, max_length=10)),
                ('send_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='eval_res',
            fields=[
                ('eval_res_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('final_res', models.CharField(max_length=100, null=True)),
                ('first_ind_res', models.CharField(max_length=1000, null=True)),
                ('second_ind_res', models.CharField(max_length=1000, null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='first_index',
            fields=[
                ('first_index_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('first_index_name', models.CharField(max_length=30, unique=True)),
                ('memo', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ind_model',
            fields=[
                ('ind_model_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ind_model_name', models.CharField(max_length=20, null=True)),
                ('ind_model_num', models.CharField(max_length=2)),
                ('ind_model_type', models.CharField(max_length=20)),
                ('ind_model_cat', models.CharField(max_length=20, null=True, unique=True)),
                ('data', models.CharField(max_length=10000)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_ind', to='evasysapp.company')),
            ],
        ),
        migrations.CreateModel(
            name='industry',
            fields=[
                ('industry_id', models.IntegerField(choices=[(1, '农林牧渔业'), (2, '采矿业'), (3, '制造业'), (4, '住宿和餐饮业'), (5, '金融业'), (6, '房地产业'), (7, '租赁和商务服务'), (8, '电力、燃气及水的生产和供应'), (9, '建筑业'), (10, '水利、环境和公共设施管理'), (11, '居民服务和其他服务'), (12, '教育'), (13, '信息传输、计算机服务和软件业'), (14, '卫生、社会保障和社会福利'), (15, '文化、体育和娱乐业'), (16, '公共管理和社会组织'), (17, '国际组织'), (18, '科学研究、技术服务和地质勘查'), (19, '交通运输、仓储和邮政'), (20, '批发和零售')], primary_key=True, serialize=False)),
                ('industry_name', models.CharField(max_length=50)),
                ('memo', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='interval',
            fields=[
                ('interval_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('interval_data', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='second_index',
            fields=[
                ('second_index_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('second_index_name', models.CharField(max_length=30, unique=True)),
                ('memo', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='third_index',
            fields=[
                ('third_index_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('third_index_name', models.CharField(max_length=30, unique=True)),
                ('memo', models.CharField(blank=True, max_length=300, null=True)),
                ('first_index_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.first_index')),
                ('second_index_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.second_index')),
            ],
        ),
        migrations.CreateModel(
            name='user_feedback',
            fields=[
                ('feedback_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('evaluation_content', models.TextField()),
                ('ctime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=6, unique=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('mobilphone', models.IntegerField(null=True, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.IntegerField(choices=[(0, '临时用户'), (1, '用户'), (2, '超级用户')])),
                ('user_authority', models.IntegerField(null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='val_model',
            fields=[
                ('val_model_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('val_model_name', models.CharField(max_length=30)),
                ('data', models.CharField(max_length=10000)),
                ('datatime', models.CharField(max_length=8, null=True)),
                ('datetype', models.IntegerField(choices=[(0, '年份'), (1, '季度'), (2, '月份')], null=True)),
                ('ctime', models.DateField(auto_now_add=True, null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_val', to='evasysapp.company')),
                ('ind_model_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_val', to='evasysapp.ind_model', to_field='ind_model_cat')),
                ('ind_model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ind_val', to='evasysapp.ind_model')),
                ('interval_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.interval')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='val_res',
            fields=[
                ('val_res_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ind_model_cat_id', models.CharField(max_length=30, null=True)),
                ('final_res', models.CharField(max_length=30, null=True)),
                ('e_res', models.CharField(max_length=30, null=True)),
                ('p_res', models.CharField(max_length=30, null=True)),
                ('period_res', models.TextField(max_length=1000, null=True)),
                ('evaluator_res', models.TextField(max_length=1000, null=True)),
                ('senior_res', models.TextField(max_length=1000, null=True)),
                ('junior_res', models.TextField(max_length=1000, null=True)),
                ('p_index_res', models.TextField(max_length=1000, null=True)),
                ('ctime', models.DateField(auto_now_add=True, null=True)),
                ('period_plot', models.TextField(null=True)),
                ('evaluator_plot', models.TextField(null=True)),
                ('senior_detail_plot', models.TextField(null=True)),
                ('algorithm_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.Algorithm_description')),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_res', to='evasysapp.company')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users')),
                ('val_model_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='evasysapp.val_model')),
            ],
        ),
        migrations.AddField(
            model_name='user_feedback',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users'),
        ),
        migrations.AddField(
            model_name='ind_model',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users'),
        ),
        migrations.AddField(
            model_name='eval_res',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users'),
        ),
        migrations.AddField(
            model_name='eval_res',
            name='val_model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evasysapp.val_model'),
        ),
        migrations.AddField(
            model_name='company',
            name='industry_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.industry'),
        ),
        migrations.AddField(
            model_name='company',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='evasysapp.users'),
        ),
    ]
