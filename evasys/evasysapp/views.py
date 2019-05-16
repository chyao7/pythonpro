# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import math

from django.shortcuts import render,redirect,HttpResponse
import time
import os

from django.template import loader, Context
from pyecharts import Page, Bar
from sympy import *
import xlrd
from evasysapp.forms import UploadExcelForm
from random import Random
from django.core.mail import send_mail
from evasysapp.models import EmailVerifyRecord
from evasys.settings import EMAIL_FROM
from evasysapp.utils_ import *
from io import BytesIO
import base64
#from xpinyin import Pinyin
from evasysapp.utils import ExtAssMethod
import json
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
from evasysapp.method import EvalCalc
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, Float):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)


def login(request):
    error_msg = ''
    if request.method =='POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if models.users.objects.filter(user_name = username,password = password):
            user_id = models.users.objects.filter(user_name = username).values("user_id")
            user_id = user_id[0]['user_id']
            request.session['username'] = username
            request.session['user_id'] = user_id
            request.session['is_login'] = True
            return redirect('http://127.0.0.1:8000/evasys/home/')
        else:
            error_msg = '用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})


def home(request):
    msgs = "游客您好,您现在使用的是试用版，若要使用完整功能请您："
    ors = '或者'
    logins = '登录'
    register = '注册'
    hidden = "hidden"
    if request.method=='GET':
        try:
            request.session['is_login']
        except:
            return render(request, 'home.html', {'huanying': msgs, 'ors': ors, 'login': logins, 'register': register,"hidden":hidden})
        if request.session['is_login']:
            username = request.session['username']
            msg = '欢迎您,' + str(username)
            return render(request, 'home.html', {'huanying': msg})
        else:
            return render(request, 'home.html', {'huanying': msgs, 'ors': ors, 'login': logins, 'register': register,"hidden":hidden})
    else:
        pass


def detail(request):
    nid = request.GET.get('nid')
    return HttpResponse(nid)


def register(request):
    industry_list = models.industry.objects.all()
    users = models.users.objects.all()
    if request.method =='POST':
        companyname = request.POST.get('companyname', None)
        liscom_code = request.POST.get('liscom_code', None)
        industry_id = int(request.POST.get('industry', None))
        telephone = request.POST.get('telephone', None)
        company_address = request.POST.get('company_address', None)
        introduction = request.POST.get('introduction', None)
        website = request.POST.get('website', None)
        docs = request.FILES.get('docs',None)
        imgs = request.FILES.get('imgs',None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        ecode = request.POST.get('emailcode',None)
        obj = models.EmailVerifyRecord.objects.get(email=email)
        vcode = obj.vcode
        send_time = obj.send_time.replace(tzinfo=None)
        user_name = obj.user_name
        nowTime = datetime.datetime.now()
        interval_time = nowTime-send_time
        if ecode == vcode and interval_time.seconds < 300:
            company_docs_path = None
            company_imgs_path = None
            for item in users:
                if item.user_name == user_name:
                    msg = '该用户已经存在，请重新输入用户名'
                    return render(request, 'register.html',{'users_msg':msg})
            if docs:
                company_docs_path = os.path.join('upload/company/docs', docs.name)
                docfile = open(company_docs_path, 'wb')
                for i in docs.chunks():
                    docfile.write(i)
                docfile.close()
            if imgs:
                company_imgs_path = os.path.join('upload/company/imgs',imgs.name)
                imgfile = open(company_imgs_path,'wb')
                for i in imgs:
                    imgfile.write(i)
                imgfile.close()
            times = time.strftime('%Y%m%d%H', time.localtime())
            p = Pinyin()
            upy = p.get_initials(username, u'')
            cpy = p.get_initials(companyname, u'')
            company_id = times+upy
            user_id = times+cpy
            models.company.objects.create(company_id = company_id,company_name = companyname,liscom_code = liscom_code,
                                          industry_id_id = industry_id,telephone = telephone,company_address = company_address,
                                          introduction = introduction,website = website,img_address = company_imgs_path,
                                          intro_address = company_docs_path)
            try:
                user = models.users(user_id = user_id,user_name =username,email = email,password= password,
                            user_type = 1)
                user.save()
            except:
                models.company.objects.filter(company_id=company_id).delete()
            return redirect('/evasys/sucregister/')
        elif vcode!= ecode:
            return render(request,'register.html',{'err_msg':'验证码错误','industry':industry_list})
        else:
            return render(request,'register.html',{'err_msg':'验证码失效','industry':industry_list})
    elif request.method =='GET':
        return render(request,'register.html',{'industry':industry_list})


def sucregister(request):
    if request.method == "GET":
        meta = request.META
        if meta.get("HTTP_REFERER")== "http://127.0.0.1:8000/evasys/register/":
            return render(request,'sucregister.html')
        else:
            return render(request,'NoPage.html')
    else:
        pass


def sendecode(request):
    user_name = request.POST.get("user_name",None)
    if len(user_name) ==0:
        msg = "用户名不能为空"
        return HttpResponse(msg)
    email = request.POST.get("email")
    users = models.users.objects.all()
    for item in users:
        if user_name == item.user_name:
            msg = '该用户已经存在，请重新输入用户名'
            return HttpResponse(msg)
        if email == item.email:
            msg = '邮箱已被注册'
            return HttpResponse(msg)
    def random_vcode(randomlength=6):
        vcode = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            vcode += chars[random.randint(0, length)]
        return vcode

    def send_register_email(email, send_type=0):
        vcode = random_vcode(6)
        email_record = EmailVerifyRecord()
        email_record.vcode_id = len(models.EmailVerifyRecord.objects.all())+1
        email_record.email = email
        email_record.user_name = user_name
        email_record.send_type = send_type
        email_record.vcode = vcode

        obj = models.EmailVerifyRecord.objects.all()
        email_list = []
        for item in obj:
            email_list.append(item.email)
        if email in email_list:
            eobj = models.EmailVerifyRecord.objects.get(email=email_record.email)
            eobj.username = user_name
            eobj.vcode = vcode
            eobj.send_type = send_type
            eobj.save()

        else:
            email_record.save()
        email_title = ""
        email_body = ""
        if send_type == 0:
            email_title = "注册验证码"
            email_body = "您的注册验证码是{0}，请妥善保管，不要透露给他人。验证码有效期为五分钟。".format(email_record.vcode)
        if send_type == 1:
            email_title = "忘记密码验证码"
            email_body = "您的验证码是{0}，请妥善保管，不要透露给他人。验证码有效期为五分钟。".format(email_record.vcode)
        if send_type == 2:
            email_title = "修改邮箱验证码"
            email_body = "您的验证码是{0}，请妥善保管，不要透露给他人。验证码有效期为五分钟。".format(email_record.vcode)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            msg = "验证码发送成功"
        else:
            msg = "验证码发送失败"
        return msg
    try:
        msg = send_register_email(email, send_type=0)
        return HttpResponse(msg)
    except Exception as e:
        return HttpResponse(e)





# def defindex(request):
#     meta = request.META
#     if request.method== "GET" and meta.get("HTTP_REFERER") == "http://127.0.0.1:8000/evasys/home/":
#         junior_index = models.junior_index.objects.all()
#         user_id = request.session.get('user_id',None)
#         companylist = models.company.objects.filter(user_id=user_id)
#         res_list = []
#         for i in range(len(junior_index)):
#             junior_index_id = junior_index[i].junior_index_id
#             memo = junior_index[i].memo
#             junior_index_name = junior_index[i].junior_index_name
#             senior_index_id = junior_index[i].senior_index_id
#             evaluator_id = junior_index[i].evaluator_id
#             period_id = junior_index[i].period_id
#             senior_index_name = models.senior_index.objects.get(senior_index_id=senior_index_id).senior_index_name
#             evaluator_name = models.evaluator.objects.get(evaluator_id=evaluator_id).evaluator_name
#             period_name = models.period.objects.get(period_id=period_id).period_name
#             res_dic = {"junior_index_id":junior_index_id,'junior_index_name':junior_index_name,'senior_index_name':senior_index_name,'evaluator_name':evaluator_name,'period_name':period_name,'memo':memo}
#             res_list.append(res_dic)
#         return render(request,'defindex.html',{'res_list':res_list,'companylist':companylist})
#     elif request.method =="POST":
#         now = datetime.datetime.now()
#         now_str = now.strftime('%Y%m%d%H%M%S')
#         data = request.POST.get("data")
#         type = request.POST.get("type")
#         company_id = request.POST.get("company_id")
#         company_name=models.company.objects.get(company_id=company_id).company_name
#
#         num = str(len(json.loads(data)))
#         user_id = request.session['user_id']
#         ind_model_id = user_id + now_str
#         user_id = models.users.objects.get(user_id=user_id)
#         ind_model_name = request.session['username']
#         obj = models.ind_model.objects.filter(user_id=user_id)
#         ind_model_cat = str('No.' + str(len(obj)+1))
#         models.ind_model.objects.create(ind_model_id=ind_model_id, ind_model_name=ind_model_name, user_id=user_id,
#                                         data=data, ind_model_type=type, ind_model_num=num,ind_model_cat=ind_model_cat,
#                                         company_id_id=company_id)
#         return redirect('/evasys/defindex/')
#     else:
#         return render(request,'NoPage.html')


def defindex(request):
    meta = request.META
    if request.method== "GET" and meta.get("HTTP_REFERER") == "http://127.0.0.1:8000/evasys/home/":
        third_index = models.third_index.objects.all()
        user_id = request.session.get('user_id',None)
        companylist = models.company.objects.filter(user_id=user_id)
        res_list = []
        print(len(third_index))
        print("ssssss")
        for i in range(len(third_index)):
            third_index_id = third_index[i].third_index_id
            memo = third_index[i].memo
            third_index_name = third_index[i].third_index_name
            second_index_id = third_index[i].second_index_id_id
            first_index_id = third_index[i].first_index_id_id
            second_index_name = models.second_index.objects.get(second_index_id=second_index_id).second_index_name
            first_index_name = models.first_index.objects.get(first_index_id=first_index_id).first_index_name
            res_dic = {"third_index_id":third_index_id,'third_index_name':third_index_name,
                       'second_index_name':second_index_name,'first_index_name':first_index_name,
                       'memo':memo}
            res_list.append(res_dic)
        print(res_list)
        return render(request,'defindex.html',{'res_list':res_list,'companylist':companylist})
    elif request.method =="POST":
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        data = request.POST.get("data")
        type = request.POST.get("type")
        company_id = request.POST.get("company_id")
        company_name=models.company.objects.get(company_id=company_id).company_name

        num = str(len(json.loads(data)))
        user_id = request.session['user_id']
        ind_model_id = user_id + now_str
        user_id = models.users.objects.get(user_id=user_id)
        ind_model_name = request.session['username']
        obj = models.ind_model.objects.filter(user_id=user_id)
        ind_model_cat = str('No.' + str(len(obj)+1))
        models.ind_model.objects.create(ind_model_id=ind_model_id, ind_model_name=ind_model_name, user_id=user_id,
                                        data=data, ind_model_type=type, ind_model_num=num,ind_model_cat=ind_model_cat,
                                        company_id_id=company_id)
        return redirect('/evasys/defindex/')
    else:
        return render(request,'NoPage.html')




def chanindex(request):
    meta = request.META
    if request.method == "GET" and meta.get("HTTP_REFERER") == "http://127.0.0.1:8000/evasys/home/":
        user_id = request.session.get('user_id', None)
        companylist = models.company.objects.filter(user_id=user_id)
        def_index = models.def_index.objects.all()
        junior_index = models.junior_index.objects.all()
        res_list = []
        for i in range(len(junior_index)):
            memo = junior_index[i].memo
            junior_index_id = junior_index[i].junior_index_id
            junior_index_name = junior_index[i].junior_index_name
            senior_index_id = junior_index[i].senior_index_id
            evaluator_id = junior_index[i].evaluator_id
            period_id = junior_index[i].period_id
            senior_index_name = models.senior_index.objects.get(senior_index_id=senior_index_id).senior_index_name
            evaluator_name = models.evaluator.objects.get(evaluator_id=evaluator_id).evaluator_name
            period_name = models.period.objects.get(period_id=period_id).period_name
            res_dic = {"junior_index_id":junior_index_id,'junior_index_name':junior_index_name,'senior_index_name':senior_index_name,'evaluator_name':evaluator_name,'period_name':period_name,'memo':memo}
            res_list.append(res_dic)
        return render(request,'chanindex.html',{'res_list':res_list,'def_index':def_index,'companylist':companylist})
    elif request.method =="POST":
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        data = request.POST.get("data")
        type = request.POST.get("type")
        num = str(len(json.loads(data)))
        user_id = request.session['user_id']
        ind_model_id = user_id + now_str
        user_id = models.users.objects.get(user_id = user_id)
        ind_model_name = request.session['username']
        obj = models.ind_model.objects.filter(user_id=user_id)
        ind_model_cat = 'No.'+str(len(obj))
        models.ind_model.objects.create(ind_model_id = ind_model_id,ind_model_name = ind_model_name,user_id = user_id,data = data,ind_model_type=type,ind_model_num=num,ind_model_cat=ind_model_cat)
        return redirect('/evasys/chanindex/')
    else:
        return render(request, "NoPage.html")


def creaindex(request):
    meta = request.META
    if request.method == "GET" and meta.get("HTTP_REFERER") == "http://127.0.0.1:8000/evasys/home/":
        user_id = request.session.get('user_id', None)
        companylist = models.company.objects.filter(user_id=user_id)
        def_index = models.def_index.objects.all()
        junior_index = models.junior_index.objects.all()
        res_list = []
        for i in range(len(junior_index)):
            memo = junior_index[i].memo
            junior_index_id = junior_index[i].junior_index_id
            junior_index_name = junior_index[i].junior_index_name
            senior_index_id = junior_index[i].senior_index_id
            evaluator_id = junior_index[i].evaluator_id
            period_id = junior_index[i].period_id
            senior_index_name = models.senior_index.objects.get(senior_index_id=senior_index_id).senior_index_name
            evaluator_name = models.evaluator.objects.get(evaluator_id=evaluator_id).evaluator_name
            period_name = models.period.objects.get(period_id=period_id).period_name
            res_dic = {"junior_index_id":junior_index_id,'junior_index_name':junior_index_name,'senior_index_name':senior_index_name,'evaluator_name':evaluator_name,'period_name':period_name,'memo':memo}
            res_list.append(res_dic)
        return render(request,'creaindex.html',{'res_list':res_list,'def_index':def_index,'companylist':companylist})
    elif request.method =="POST":
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        data = request.POST.get("data")
        data_type = request.POST.get("type")
        company_id = request.POST.get("companyid")
        company_name = models.company.objects.get(company_id=company_id).company_name
        num = str(len(json.loads(data)))
        user_id = request.session.get('user_id',None)
        ind_model_id = user_id + now_str
        user_id = models.users.objects.get(user_id = user_id)
        ind_model_name = request.session.get('username',None)
        obj = models.ind_model.objects.filter(user_id=user_id)

        ind_model_cat = str('No.' + str(len(obj) + 1))
        models.ind_model.objects.create(company_id_id=company_id, ind_model_id=ind_model_id,
                                        ind_model_name=ind_model_name, user_id=user_id, data=data,
                                        ind_model_type=data_type, ind_model_num=num, ind_model_cat=ind_model_cat)
        models.def_index.objects.all().delete()
        return render(request, 'creaindex.html')
    else:
        return render(request, "NoPage.html")


def newindex(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        memo = request.POST.get('memo')
        evaluator_id_id = request.POST.get('evaluator_id_id')
        print('evaluator_id_id',evaluator_id_id)
        junior_index_name = request.POST.get('junior_index_name')
        period_id_id = request.POST.get('period_id_id')
        print('period_id_id',period_id_id)
        senior_index_name = request.POST.get('senior_index_name')
        exist_senior = models.senior_index.objects.filter(senior_index_name=senior_index_name)
        exist_def_senior = models.def_index.objects.filter(senior_index_name=senior_index_name)
        exist_junior = models.junior_index.objects.filter(junior_index_name=junior_index_name)
        exist_def_junior = models.def_index.objects.filter(junior_index_name=junior_index_name)
        evaluator_name = models.evaluator.objects.get(evaluator_id=evaluator_id_id).evaluator_name
        period_name = models.period.objects.get(period_id=period_id_id).period_name
        if exist_junior:
            ret['status'] = False
            ret['error'] = "二级指标已存在"
        elif exist_def_junior:
            ret['status'] = False
            ret['error'] = "自定义二级指标重复"
        elif senior_index_name=="":
            ret['status'] = False
            ret['error'] = "一级指标不能为空"
        elif junior_index_name=="":
            ret['status'] = False
            ret['error'] = "二级指标不能为空"
        else:
            if exist_senior:
                senior_index_id = exist_senior[0]
                print(senior_index_id)
            elif exist_def_senior:
                index_id = exist_def_senior[0]
                senior_index_id = index_id[2:4]
            else:
                senior_index_id = len(models.def_index.objects.all())+21
            junior_index_id =period_id_id + evaluator_id_id+str(senior_index_id) +str(len(models.def_index.objects.all())+len(models.junior_index.objects.all()))
            junior_index_name = junior_index_name
            res_dic = {"junior_index_id": junior_index_id, 'junior_index_name': junior_index_name,
                       'senior_index_name': senior_index_name, 'evaluator_name': evaluator_name,
                       'period_name': period_name, 'memo': 'None'}
            try:
                models.def_index.objects.create(**res_dic)
            except Exception as e:
                print(e)
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    return HttpResponse(json.dumps(ret))


def indexval(request):
    ind_model_name = request.session.get("username", None)
    obj = models.ind_model.objects.filter(ind_model_name=ind_model_name)
    if request.method =="GET":
        intervals = models.interval.objects.all()
        res_list = []
        datas = []
        for i in range(len(obj)):
            data = obj[i].data
            datas.append(json.loads(data))
        return render(request, "indexval.html", {'res_list': obj, "datas": datas,'intervals':intervals})
    elif request.method =="POST":
        if request.POST.get("data",None):
            datatime = request.POST.get("cycle", None)
            datetype = request.POST.get("datetype", None)
            interval_id = request.POST.get("interval_id", None)
            interval = models.interval.objects.get(interval_id=interval_id)
            now = datetime.datetime.now()
            now_str = now.strftime('%Y%m%d%H%M%S')
            user_id = request.session['user_id']
            val_model_id = user_id + "ValModel" + now_str
            user_id = models.users.objects.get(user_id=user_id)
            ind_model_id = request.POST.get("id")
            ind_model = models.ind_model.objects.get(ind_model_id=ind_model_id)
            ind_model_cat = ind_model.ind_model_cat
            company_id = ind_model.company_id_id

            data = json.loads(request.POST.get("data"))
            val_model_name = request.session['username']
            pre_data = json.loads(ind_model.data)
            for i,item in enumerate(pre_data):
                if item in data:
                    pre_data[item].append(data[item])
            try:
                models.val_model.objects.create(company_id_id=company_id,ind_model_cat_id=ind_model_cat
                                            ,val_model_id = val_model_id,ind_model_id = ind_model
                                            ,val_model_name = val_model_name,user_id = user_id
                                            ,data = json.dumps(pre_data),datetype=datetype
                                            ,datatime=datatime,interval_id=interval)
            except Exception as e:
                print(e)
            return HttpResponse("ok")
        elif request.POST.get("ids",None):
            ids = request.POST.get("ids")
            ids_json = json.loads(ids)
            for item,i in enumerate(ids_json):
                ind_model_id = ids_json[i]
                models.ind_model.objects.get(ind_model_id = ind_model_id).delete()
        return HttpResponse("OK")

'''
def calculate(request):
    if request.method =="GET":
        val_model_name = request.session.get("username", None)
        algorithms = models.Algorithm_description.objects.all()
        obj = models.val_model.objects.filter(val_model_name = val_model_name)
        ii = models.val_model.objects.filter(val_model_name = val_model_name).values_list('val_model_id','data')
        datas = []
        for i in range(len(obj)):
            data = obj[i].data
            datas.append(json.loads(data))
        return render(request, "calculate.html", {'res_list': obj, "datas": datas,'algorithms':algorithms})
    elif request.method =="POST":
        if request.POST.get("ids",None):
            ids = request.POST.get("ids")
            ids_json = json.loads(ids)
            for item,i in enumerate(ids_json):
                val_model_id = ids_json[i]
                try:
                    models.val_res.objects.get(val_model_id = val_model_id).delete()
                except:
                    pass
                models.val_model.objects.get(val_model_id = val_model_id).delete()
            return redirect("/evasys/resvisualization/")
        elif request.POST.get("cal_ids",None):
            user_id = request.session.get("user_id",None)
            userInstance = models.users.objects.get(user_id=user_id)
            val_model_id = json.loads(request.POST.get("cal_ids"))
            algorithm_id = request.POST.get("alg_id")
            algorithmInstance = models.Algorithm_description.objects.get(algorithm_id=algorithm_id)

            now = datetime.datetime.now()
            now_str = now.strftime('%Y%m%d%H%M%S')
            val_res_id = user_id+"ValRes"+now_str
            if algorithm_id=='1':
                for i in range(len(val_model_id)):
                    valModelInstance = models.val_model.objects.get(val_model_id=val_model_id[i])
                    companyId = valModelInstance.company_id
                    ind_model_cat_id = valModelInstance.ind_model_cat_id
                    interval_id = valModelInstance.interval_id
                    intervalObj = models.interval.objects.get(interval_id=interval_id)
                    intervalStr = intervalObj.interval_data
                    intervalList = list(map(int, intervalStr.split(",")))
                    evaDF, seniorResDF, evaluatorResDF, periodResDF, totalScoreDict= ExtAssMethod(dataJson=valModelInstance.data,
                                                                            jingDianYuList=intervalList).addresDict()
                    print(periodResDF)
                    try:
                        periodResJson = json.dumps(periodResDF.to_dict(), cls=MyEncoder)
                        evaluatorResJson =json.dumps(evaluatorResDF.to_dict(), cls=MyEncoder)
                        seniorResJson =  json.dumps(seniorResDF.to_dict(), cls=MyEncoder)
                    except Exception as e:
                        print(e, "calculate wrong")
                        periodResJson, evaluatorResJson, seniorResJson, totalScoreDict = None, None,None, None

                    if periodResJson is not None:
                        try:
                            models.val_res.objects.create(final_res=totalScoreDict["t"], period_res=periodResJson,
                                                          evaluator_res=evaluatorResJson,senior_res=seniorResJson,
                                                          user_id=userInstance, val_model_id=valModelInstance,
                                                          algorithm_id=algorithmInstance,company_id=companyId,
                                                          val_res_id=val_res_id,ind_model_cat_id=ind_model_cat_id)
                        except Exception as e:
                            print(e, "model wrong")
                            return HttpResponse("Bad Request")
                    else:
                        print("calculate Wrong")
                        return HttpResponse("Bad Request")
                return HttpResponse("OK")
            else:
                value_list = []
                for i in range(len(val_model_id)):
                    obj = models.val_model.objects.get(val_model_id=val_model_id[i])
                    data_dic = json.loads(obj.data)
                    v_list=[]
                    global k_list
                    k_list = list(data_dic.keys())
                    for v in data_dic.values():
                        v_list.append(float(v[4]))
                    value_list.append(v_list)
                df = pd.DataFrame(value_list, columns=k_list).T
                data_values=df.values
            if algorithm_id == '2':
                cv_w = CV(data_values)
                print('变异系数法权重：',cv_w)
                cv_v = CaculateValue(data_values, cv_w)
                print('变异系数法结果:',cv_v)
                res = {'cv_w':list(cv_w),'cv_v':cv_v}
            if algorithm_id == '3':
                en_w = EntropyMethod(data_values)
                print('熵值法权重：',en_w)
                en_v = CaculateValue(data_values, en_w)
                print('熵值法结果:',en_v)
                res = {'w':list(en_w),'v':en_v}
            if algorithm_id == '6':
                cr_w = Critic(data_values)
                print('Critic法权重：',cr_w)
                cr_v = CaculateValue(data_values, cr_w)
                print('Critic法结果:',cr_v)
                res = {'w':list(cr_w),'v':cr_v}
            if algorithm_id == '6':
                me_w = MeanError(df.values)
                print('标准离差法权重：',me_w)
                me_v = CaculateValue(df.values, me_w)
                print('标准离差法结果:',me_v)
                res = {'w':list(me_w),'v':me_v}
            now = datetime.datetime.now()
            now_str = now.strftime('%Y%m%d%H%M%S')
            val_res_id = user_id + now_str
            result = json.dumps(res)
            models.val_res.objects.create(junior_res=result,algorithm_id_id=algorithm_id,val_model_id=val_model_id,val_res_id=val_res_id,user_id_id=user_id,ind_model_cat_id=ind_model_cat_id)
            return HttpResponse('ok')
'''

def calculate(request):
    if request.method =="GET":
        val_model_name = request.session.get("username", None)
        obj = models.val_model.objects.filter(val_model_name = val_model_name)
        datas = []
        for i in range(len(obj)):
            data = obj[i].data
            datas.append(json.loads(data))
        return render(request, "calculate.html", {'res_list': obj, "datas": datas})
    elif request.method =="POST":
        if request.POST.get("ids",None):
            ids = request.POST.get("ids")
            ids_json = json.loads(ids)
            for i in ids_json:
                val_model_id = ids_json[i]
                try:
                    models.val_res.objects.get(val_model_id = val_model_id).delete()
                except:
                    pass
                models.val_model.objects.get(val_model_id = val_model_id).delete()
            return redirect("/evasys/resvisualization/")
        elif request.POST.get("cal_ids",None):
            user_id = request.session.get("user_id",None)
            userInstance = models.users.objects.get(user_id=user_id)
            # global ind_model_id
            val_model_id = json.loads(request.POST.get("cal_ids"))
            print(val_model_id)
            now = datetime.datetime.now()
            now_str = now.strftime('%Y%m%d%H%M%S')
            val_res_id = user_id+"EvalRes"+now_str
			
            datas = []
            companies = []
            for i in range(len(val_model_id)):
                valModelInstance = models.val_model.objects.get(val_model_id=val_model_id[i])
                companyId = valModelInstance.company_id
                ind_model_cat_id = valModelInstance.ind_model_cat_id
                companyname = models.company.objects.get(company_id=companyId).company_name
                data = valModelInstance.data
                data = json.loads(data)
                companies.append(companyname)
                datas.append(data)    			
            first_ind_res, second_ind_res, final_res = EvalCalc(datas, companies).excute()
            print(first_ind_res, second_ind_res, final_res)
            try:
                firstResJson = json.dumps(first_ind_res.to_dict('index'))
                secondResJson = json.dumps(second_ind_res.to_dict('index'))
                finalResJson =  json.dumps(final_res.to_dict('index'))
            except Exception as e:
                print(e, "calculate wrong")
                firstResJson, secondResJson, finalResJson = None, None, None
                return HttpResponse("Bad Request")
				
            try:
                models.val_res.objects.create(final_res=finalResJson, second_ind_res=secondResJson,
                                                          first_ind_res=firstResJson,
                                                          user_id=userInstance, val_model_id=valModelInstance,
                                                          company_id=companyId,
                                                          val_res_id=val_res_id,ind_model_cat_id=ind_model_cat_id)
            except Exception as e:
                print(e, "model wrong")
                return HttpResponse("Bad Request")
        return HttpResponse("OK")	


def charts(data):
    style = dict(
        is_datazoom_show=True,
        datazoom_range=[0, 100],
        xaxis_type='category',
        is_xaxislabel_align=True,
        xaxis_label_textsize=16,
        yaxis_label_textsize=16,
        xaxis_name_size=20,
        yaxis_name_size=20,
        xaxis_name='评价对象',

        yaxis_name='得分',
        legend_pos='right',
        legend_top='3%',
        xaxis_name_pos='end',
        is_label_show=True,
        mark_line=['average'],
        mark_point=['min', 'max']
    )
    page = Page()
    data_object = data.index.values.tolist()
    data_indicators = data.columns.values.tolist()
    for i in data_indicators:
        x = data[i].sort_values(ascending=False)
        bar = Bar(i,width=1000)
        bar.add(i, x.index.tolist(), x.values.tolist(), **style)
        page.add(bar)
    return page

def resvisualization(request):

    if request.method == "GET" and request.GET.get("id", None):
        val_res_id = request.GET.get("id",None)
        final = pd.DataFrame(json.loads(models.val_res.objects.get(val_res_id=val_res_id).final_res)).T
        first = pd.DataFrame(json.loads(models.val_res.objects.get(val_res_id=val_res_id).first_ind_res)).T
        second = pd.DataFrame(json.loads(models.val_res.objects.get(val_res_id=val_res_id).second_ind_res)).T
        line_second = charts(second)
        line_first = charts(first)
        line_final = charts(final)
        context = dict(
            myechart1=line_second.render_embed(),
            myechart2=line_first.render_embed(),
            myechart3 = line_final.render_embed(),
            script_list=line_second.get_js_dependencies()
            )
        print(line_second.get_js_dependencies())
        line_second.get_js_dependencies()
        return render(request,"resvisualization.html",context)








def resshow(request):
    if request.method=="GET":
        user_id = request.session.get("user_id",None)
        username = request.session.get("username",None)
        obj = models.val_res.objects.filter(user_id=user_id)
        res_list = []
        for i in range(len(obj)):
            val_res_id = obj[i].val_res_id
            val_model = obj[i].val_model_id
            final_res = obj[i].final_res
            ctime = obj[i].ctime
            res_dict = {"val_res_id":val_res_id,"val_model_id":val_model,"final_res":final_res,"ctime":ctime,"username":username}
            res_list.append(res_dict)
        return render(request,"resshow.html",{"res_list":obj})
    elif request.method =="POST":
        if request.POST.get("ids",None):
            ids = request.POST.get("ids")
            ids_json = json.loads(ids)
            for item,i in enumerate(ids_json):
                val_res_id = ids_json[i]
                models.val_res.objects.get(val_res_id = val_res_id).delete()
        return redirect("/evasys/resvisualization/")


def modscope(request):
    try:
        inf = request.META['HTTP_REFERER']
    except:
        return HttpResponse("BAD REQUEST")
    if inf ==  'http://127.0.0.1:8000/evasys/home/':
        return render(request,'modscope.html')


def modalgorithm(request):
    return render(request,'modalgorithm.html')


def moddescribe(request):
    return render(request,'moddescribe.html')


def modevaluation(request):
    return render(request,'modevaluation.html')


def EXEMtheory(request):
    return render(request,'EXEMtheory.html')


def EXEMfeature(request):
    return render(request,'EXEMfeature.html')


def EXEMmodel(request):
    return render(request,'EXEMmodel.html')


def EWMtheory(request):
    return render(request,'EWMtheory.html')


def EWMfeature(request):
    return render(request,'EWMfeature.html')


def EWMmodel(request):
    return render(request,'EWMmodel.html')
def AHPtheory(request):
    return render(request,'AHPtheory.html')


def AHPfeature(request):
    return render(request,'AHPfeature.html')


def AHPmodel(request):
    return render(request,'AHPmodel.html')


def CMtheory(request):
    return render(request,'CMtheory.html')


def CMfeature(request):
    return render(request,'CMfeature.html')


def CMmodel(request):
    return render(request,'CMmodel.html')


def getexcel(request):
    user_id = request.session.get('user_id')
    companylist = models.company.objects.filter(user_id_id=user_id)
    companyid=request.POST.get("companyid",None)
    intervals = models.interval.objects.all()
    if request.method == "POST" and companyid is None:
        form = UploadExcelForm(request.POST, request.FILES)
        res_list = []
        if form.is_valid():
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            table = wb.sheets()[0]
            row = table.nrows
            val_list=[]
            index_list=[]
            for i in range(1,row):
                col = table.row_values(i)
                period_name = col[0]
                evaluator_name = col[1]
                senior_index_name = col[2]
                junior_index_name = col[3]
                val = col[4]
                res_dic = {'period_name':period_name,'evaluator_name':evaluator_name,'senior_index_name':senior_index_name,'junior_index_name':junior_index_name,'val':val}
                res_list.append(res_dic)
                val_list.append(val)
                index_list.append(col[:4])
            ind_model_obj = models.ind_model.objects.filter(user_id=user_id)
            def get_index_id(obj, index_list):
                for i in range(len(obj)):
                    data = json.loads(obj[i].data)
                    if list(data.values()) == index_list:
                        ind_model_id = obj[i].ind_model_id
                        pre_data = json.loads(obj[i].data)
                        ind_model = obj[i]
                        return ind_model_id, pre_data, ind_model
            ind_model_id, pre_data, ind_model = get_index_id(ind_model_obj, index_list)
            ind_model = models.ind_model.objects.get(ind_model_id=ind_model_id)
            pre_data = json.loads(ind_model.data)
            for i, item in enumerate(pre_data):
                res_list[i]['junior_index_id']=item
            return render(request, 'getexcel.html', {'res_list': res_list,'ind_model_id':ind_model_id
                , 'companylist': companylist,"intervals":intervals})
    if companyid:
        datatime = request.POST.get("datatime",None)
        datetype = request.POST.get("datetype",None)
        ind_model_id = request.POST.get("ind_model_id",None)
        interval_id = request.POST.get("interval_id",None)
        data = request.POST.get("data",None)
        val_model_name = request.session['username']
        ind_model = models.ind_model.objects.get(ind_model_id=ind_model_id)
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        val_model_id = user_id + now_str
        models.val_model.objects.create(val_model_id=val_model_id, ind_model_id_id=ind_model_id,
                                        val_model_name=val_model_name, user_id_id=user_id,
                                        data=data, ind_model_cat_id=ind_model.ind_model_cat
                                        ,datatime=datatime,datetype=datetype,interval_id_id=interval_id
                                        ,company_id_id=companyid)
        return render(request,'getexcel.html',{'companylist':companylist,"intervals":intervals})
    elif request.method == "GET":
        return render(request,'getexcel.html',{'companylist':companylist,'intervals':intervals})


def sendecode_email_change(request):
    user_id = request.session['user_id']
    user_name=models.users.objects.get(user_id=user_id).user_name
    email = request.POST.get("email")
    users = models.users.objects.all()
    for item in users:
        if email == item.email:
            msg = '邮箱已被注册'
            return HttpResponse(msg)

    def random_vcode(randomlength=6):
        vcode = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            vcode += chars[random.randint(0, length)]
        return vcode

    def send_register_email(email, send_type=0):
        vcode = random_vcode(6)
        email_record = EmailVerifyRecord()
        email_record.vcode_id = len(models.EmailVerifyRecord.objects.all()) + 1
        email_record.email = email
        email_record.user_name = user_name
        email_record.send_type = send_type
        email_record.vcode = vcode

        obj = models.EmailVerifyRecord.objects.all()
        email_list = []
        for item in obj:
            email_list.append(item.email)
        if email in email_list:
            eobj = models.EmailVerifyRecord.objects.get(email=email_record.email)
            eobj.username = user_name
            eobj.vcode = vcode
            eobj.send_type = send_type
            eobj.save()

        else:
            email_record.save()
        email_title = ""
        email_body = ""
        if send_type == 0:
            email_title = "注册验证码"
            email_body = "您的注册验证码是{0}，请妥善保管，不要透露给他人。验证码有效期为五分钟。".format(email_record.vcode)
        if send_type == 1:
            email_title = "忘记密码验证码"
            email_body = "您的验证码是{0}，请妥善保管，不要透露给他人。验证码有效期为五分钟。".format(email_record.vcode)
        if send_type == 2:
            email_title = "修改邮箱验证码"
            email_body = "您的验证码是{0}，请妥善保管，不要透露给他人。验证码有效期为五分钟。".format(email_record.vcode)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            msg = "验证码发送成功"
        else:
            msg = "验证码发送失败"
        return msg

    try:
        msg = send_register_email(email, send_type=0)
        return HttpResponse(msg)
    except Exception as e:
        print(e)
        return HttpResponse(e)


def Usercenter(request):
    user_id = request.session['user_id']
    users = models.users.objects.get(user_id=user_id)
    if request.method=="GET":
        user_name=users.user_name
        email=users.email
        creat_time=users.createtime
        uptime=users.updatetime
        return render(request,'Usercenter.html',{'user_name':user_name,'email':email,'creat_time':creat_time,'uptime':uptime})


def company_info(request):
    industry = models.industry.objects.all()
    user_id = request.session['user_id']
    company = models.company.objects.filter(user_id=user_id)
    if request.method=="GET":
       return render(request,'company_info.html',{'industry':industry,'companys':company,})
    if request.method=="POST":
        count = len(models.company.objects.all())
        companyname = request.POST.get('companyname', None)
        liscom_code = request.POST.get('liscom_code', None)
        industry_id = request.POST.get('industry', None)
        telephone = request.POST.get('telephone', None)
        company_address = request.POST.get('company_address', None)
        introduction = request.POST.get('introduction', None)
        website = request.POST.get('website', None)
        company_del_id = request.POST.get('company_del_id',None)
        if industry_id:
            for item in company:
                if item.company_name == companyname:
                    error_msg = '该企业已经关联，请重新输入企业名称'
                    return HttpResponse(error_msg)
            times = time.strftime('%Y%m%d%H%M%S', time.localtime())
            company_id = times + str(count)
            industry = models.industry.objects.get(industry_id=industry_id)
            user = models.users.objects.get(user_id=user_id)
            models.company.objects.create(company_id=company_id, company_name=companyname, liscom_code=liscom_code,
                                          industry_id=industry, telephone=telephone,
                                          company_address=company_address,
                                          introduction=introduction, website=website, user_id=user)
        else:
            models.company.objects.filter(company_id=company_del_id).delete()
            company = models.company.objects.filter(user_id=user_id)
        return redirect('/evasys/company_info/')


def company_del(request):
    if request.method=="POST":
        company_del_id=request.POST.get('company_del_id')
        models.company.objects.filter(company_id=company_del_id).delete()
    return HttpResponse('删除成功')


def email_info(request):
    user_id = request.session['user_id']
    users = models.users.objects.get(user_id=user_id)
    email = users.email
    if request.method=="GET":
        email = users.email
        return render(request,'email_info.html',{'email':email})
    if request.method=="POST":
        ecode=request.POST.get('Verification_Code')
        email = request.POST.get('new_email', None)
        obj = models.EmailVerifyRecord.objects.get(email=email)
        vcode = obj.vcode
        send_time = obj.send_time.replace(tzinfo=None)
        nowTime = datetime.datetime.now()
        interval_time = nowTime - send_time
        if ecode == vcode and interval_time.seconds < 300:
            users.email=email
            users.save()
            return HttpResponse("修改成功")
        elif vcode!=ecode:
            return HttpResponse('验证码错误')
        else:
            return  HttpResponse("验证码失效")


def code_info(request):
    user_id = request.session['user_id']
    users=models.users.objects.get(user_id=user_id)
    code = users.password
    if request.method=="POST":
        original_code=request.POST.get('original_code',None)
        new_code=request.POST.get('repassword',None)
        if code==original_code:
            users.password=new_code
            users.save()
            err_msg = "修改成功"
            return render(request, 'code_info.html', {"success_msg": err_msg})
        else:
            err_msg="原来密码输入错误"
            return render(request,'code_info.html',{"success_msg":err_msg})
    if request.method=="GET":
        return render(request,'code_info.html')


def user_feedback(request):
    if request.method=="GET":
        return render(request,'user_feedback.html')
    if request.method=="POST":
        user_id = request.session['user_id']
        times = time.strftime('%Y%m%d%H%M%S', time.localtime())
        feedback_id=user_id+times
        evaluation_content=request.POST.get('evaluation',None)
        models.user_feedback.objects.create(feedback_id=feedback_id,evaluation_content=evaluation_content,user_id_id=user_id)
        return HttpResponse('提交成功')


def historical_eval(request):
    if request.method=="GET":
        user_id = request.session['user_id']
        historical_eval=models.user_feedback.objects.filter(user_id=user_id)
        return render(request, 'historical_eval.html',{'historical_eval':historical_eval})
    if request.method=="POST":
        feedback_id=request.POST.get("evaluation",None)
        models.user_feedback.objects.get(feedback_id=feedback_id).delete()
        return HttpResponse('删除成功')

