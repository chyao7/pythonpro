# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class industry(models.Model):
    industry_id_choice = (
        (1,'农林牧渔业'),
        (2,'采矿业'),
        (3,'制造业'),
        (4,'住宿和餐饮业'),
        (5,'金融业'),
        (6, '房地产业'),
        (7, '租赁和商务服务'),
        (8, '电力、燃气及水的生产和供应'),
        (9, '建筑业'),
        (10, '水利、环境和公共设施管理'),
        (11, '居民服务和其他服务'),
        (12, '教育'),
        (13, '信息传输、计算机服务和软件业'),
        (14, '卫生、社会保障和社会福利'),
        (15, '文化、体育和娱乐业'),
        (16, '公共管理和社会组织'),
        (17, '国际组织'),
        (18, '科学研究、技术服务和地质勘查'),
        (19, '交通运输、仓储和邮政'),
        (20, '批发和零售'),
    )
    industry_id = models.IntegerField(choices=industry_id_choice,primary_key= True)
    industry_name = models.CharField(max_length=50)
    memo = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.industry_name


class company(models.Model):
    company_id = models.CharField(max_length=18,primary_key=True)
    company_name = models.CharField(max_length=40,unique=True)
    liscom_code = models.CharField(max_length=6,default=0)
    company_address = models.CharField(max_length=100)
    industry_id = models.ForeignKey("industry",on_delete = models.CASCADE,to_field='industry_id',null = True)
    user_id = models.ForeignKey("users",to_field='user_id',on_delete=models.CASCADE,null=True)
    telephone = models.CharField(max_length=20)
    introduction = models.CharField(max_length=500)
    website = models.CharField(max_length=100,null=True)
    img_address = models.CharField(max_length=100,null=True)
    intro_address = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.company_id

class users(models.Model):
    usertype_list = (
        (0,'临时用户'),
        (1, '用户'),
        (2, '超级用户'),
    )
    user_id = models.CharField(max_length=18,primary_key=True)
    user_name = models.CharField(max_length=6,unique=True)
    email = models.CharField(max_length=30,unique=True)
    mobilphone = models.IntegerField(null=True,unique=True)
    password = models.CharField(max_length=20)
    user_type = models.IntegerField(choices=usertype_list)
    user_authority = models.IntegerField(null=True)
    createtime = models.DateTimeField(auto_now_add=True,null=True)
    updatetime = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.user_id

class EmailVerifyRecord(models.Model):
    vcode_id = models.CharField(max_length=5,primary_key=True)
    user_name = models.CharField(max_length=6,null=True)
    email = models.CharField(max_length=30, unique=True)
    vcode = models.CharField(max_length=18)
    send_type = models.CharField(max_length=10,choices=((0,u"注册"), (1,u"找回密码"),(2,u"修改邮箱")),default=0)
    send_time = models.DateTimeField(auto_now=True,null=True)

class Algorithm_description(models.Model):
    algorithm_id=models.CharField(max_length=20,primary_key=True)
    algorithm_name=models.CharField(max_length=100)
    algorithm_type=models.CharField(max_length=4,null=True)
    algorithm_img=models.ImageField(null=True)
    algorithm_text=models.CharField(max_length=10000,null=True)
    def __str__(self):
        return self.algorithm_id
'''
class period(models.Model):
    period_id = models.CharField(max_length=1,primary_key=True)
    period_name = models.CharField(max_length=30,unique=True)
    memo = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.period_id

class evaluator(models.Model):
    evaluator_id = models.CharField(max_length=1,primary_key = True)
    evaluator_name = models.CharField(max_length=30,unique=True)
    memo = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.evaluator_id

class senior_index(models.Model):
    senior_index_id = models.CharField(max_length=2,primary_key = True)
    senior_index_name = models.CharField(max_length=30,unique=True)
    memo = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.senior_index_id

class junior_index(models.Model):
    junior_index_id = models.CharField(max_length=6,primary_key = True)
    junior_index_name = models.CharField(max_length=30,unique=True)
    period_id = models.ForeignKey("period", to_field="period_id", null=True,on_delete = models.CASCADE)
    evaluator_id = models.ForeignKey("evaluator", to_field="evaluator_id", null=True,on_delete = models.CASCADE)
    senior_index_id = models.ForeignKey('senior_index',to_field='senior_index_id',null=True,on_delete = models.CASCADE)
    memo = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.junior_index_name
'''
class ind_model(models.Model):
    ind_model_id = models.CharField(primary_key=True,max_length=100)
    ind_model_name = models.CharField(max_length=20,null=True)
    ind_model_num = models.CharField(max_length=2)
    ind_model_type = models.CharField(max_length=20)
    ind_model_cat = models.CharField(max_length=20,null=True,unique=True)
    user_id = models.ForeignKey('users',to_field='user_id',null=True,on_delete = models.CASCADE)
    company_id = models.ForeignKey("company", to_field="company_id",null=True,on_delete = models.CASCADE,related_name='id_ind')
    data = models.CharField(max_length=10000)
    ctime = models.DateTimeField(auto_now_add=True,null = True)
    def __str__(self):
        return self.ind_model_name

class val_model(models.Model):
    datetype_choices =(
        (0, u'年份'),
        (1, u"季度"),
        (2, u"月份"),
    )
    val_model_id = models.CharField(max_length=50,primary_key=True)
    val_model_name = models.CharField(max_length=30)
    ind_model_id = models.ForeignKey("ind_model",to_field="ind_model_id",on_delete = models.CASCADE,related_name='ind_val')
    ind_model_cat = models.ForeignKey("ind_model",to_field="ind_model_cat",on_delete = models.CASCADE,related_name='cat_val',null=True)
    user_id = models.ForeignKey("users",to_field="user_id",on_delete = models.CASCADE)
    company_id=models.ForeignKey("company",to_field="company_id",null=True,on_delete = models.CASCADE,related_name='id_val')
    data = models.CharField(max_length=10000)
    datatime = models.CharField(max_length=8,null=True)
    datetype = models.IntegerField(choices=datetype_choices,null=True)
    interval_id = models.ForeignKey('interval', to_field='interval_id', on_delete=models.CASCADE, null=True)
    ctime = models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.val_model_id

class val_res(models.Model):
    val_res_id = models.CharField(max_length=50,primary_key=True)
    val_model_id = models.ForeignKey("val_model", to_field="val_model_id", on_delete=models.DO_NOTHING,)
    ind_model_cat_id = models.CharField(max_length=30,null=True)
    final_res = models.CharField(max_length=1000,null=True)
    second_ind_res = models.CharField(max_length=10000,null=True)
    first_ind_res = models.CharField(max_length=10000,null=True)
    #e_res = models.CharField(max_length=30,null=True)
    #p_res = models.CharField(max_length=30,null=True)
    user_id = models.ForeignKey("users",to_field="user_id",on_delete = models.CASCADE)
    #algorithm_id = models.ForeignKey("Algorithm_description",to_field="algorithm_id",null=True,on_delete = models.CASCADE)
    company_id = models.ForeignKey("company", to_field="company_id",null=True,on_delete = models.CASCADE,related_name='id_res')
    #period_res = models.TextField(max_length=1000,null=True)
    #evaluator_res = models.TextField(max_length = 1000,null=True)
    #senior_res = models.TextField(max_length=1000,null=True)
    #junior_res = models.TextField(max_length=1000,null=True)
    #p_index_res = models.TextField(max_length=1000,null=True)
    ctime = models.DateField(auto_now_add=True,null=True)
    period_plot=models.TextField(null=True)
    evaluator_plot=models.TextField(null=True)
    senior_detail_plot=models.TextField(null=True)

class interval(models.Model):
    interval_id = models.CharField(max_length=10,primary_key=True)
    interval_data = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.interval_id

class def_index(models.Model):
    junior_index_id=models.CharField(max_length=6,primary_key=True)
    period_name=models.CharField(max_length=30,null=True)
    evaluator_name=models.CharField(max_length=30,null=True)
    junior_index_name=models.CharField(max_length=30,null=True)
    senior_index_name=models.CharField(max_length=30,null=True)
    memo=models.CharField(max_length=30,default=None)
    def __str__(self):
        return self.junior_index_id

class user_feedback(models.Model):
    feedback_id = models.CharField(max_length=32,primary_key=True)
    user_id = models.ForeignKey("users",to_field="user_id",on_delete = models.CASCADE)
    evaluation_content=models.TextField()
    ctime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.feedback_id

#创建评价指标体系涉及数据表
class first_index(models.Model):
    first_index_id = models.CharField(max_length=2,primary_key=True)
    first_index_name = models.CharField(max_length=30,unique=True)
    memo = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.first_index_id

class second_index(models.Model):
    second_index_id = models.CharField(max_length=2,primary_key = True)
    second_index_name = models.CharField(max_length=30,unique=True)
    memo = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.second_index_id

class third_index(models.Model):
    third_index_id = models.CharField(max_length=6,primary_key = True)
    third_index_name = models.CharField(max_length=30,unique=True)
    second_index_id = models.ForeignKey("second_index", to_field="second_index_id", null=True,on_delete = models.CASCADE)
    first_index_id = models.ForeignKey("first_index", to_field="first_index_id", null=True,on_delete = models.CASCADE)
    memo = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.third_index_id

class eval_res(models.Model):
    eval_res_id = models.CharField(max_length=50,primary_key=True)
    val_model_id = models.ForeignKey("val_model", to_field="val_model_id", on_delete=models.CASCADE)
    final_res = models.CharField(max_length=100,null=True)
    user_id = models.ForeignKey("users",to_field="user_id",on_delete = models.CASCADE)
    first_ind_res = models.CharField(max_length=1000,null=True)
    second_ind_res = models.CharField(max_length=1000,null=True)
    company_id = models.ForeignKey('company',to_field='company_id',null=True,on_delete = models.CASCADE)
    def __str__(self):
        return self.eval_res_id