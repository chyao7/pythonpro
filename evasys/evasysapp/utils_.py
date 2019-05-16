import numpy as np
import pandas as pd
import datetime
import json
from evasysapp import models
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

# 数据标准化
# Z-score
def Z_ScoreNormalization(M):
    M_hat = []
    for x in M:
        print(x)
        mu = np.mean(x)
        sigma = np.std(x)
        if sigma > 0:
            x = (x - mu) / sigma
        else:
            x = x - mu
        M_hat.append(list(x))
    return M_hat


###知道权重后计算值
def CaculateValue(M, weight):
    v = []
    m = (np.mat(M)).T
    for i in m:
        v.append(np.sum(np.array(i) * weight))
    return v


# 变异系数法
def CV(M):
    # Coefficient of Variance
    # M是一个二维数组
    # 返回一个权重向量
    Coef = []
    for x in M:
        if np.mean(x) == 0:
            return 0
        i = np.std(x) / np.mean(x)
        Coef.append(i)
    if sum(Coef) == 0:
        return np.ones(len(M)) / len(M)
    else:
        return Coef / sum(Coef)

# 熵值法
# 原始数据进行归一化，得到标准化后的矩阵
def Entropy(X):
    p = np.array(X) / sum(X)
    return (-1) * sum(p * np.log(p))


def EntropyMethod(M):
    # M为一个二维数组
    # M[i]表示第i个指标的取值
    if len(M) == 1:
        return [1.0]
    d_info = []
    for x in M:
        d = 1 - Entropy(x) / np.log(len(M))
        d_info.append(d)
    return d_info / sum(d_info)


# 主成分分析法
# principal component analysis
def PCA_Method(M):
    # M是经过Z-score标准化处理后的一个二维数组
    R = np.corrcoef(M)
    R = np.mat(R)
    a, b = np.linalg.eig(R)  # 得到特征值a和特征向量矩阵b
    weight = abs(a) / sum(abs(a))  #
    return weight, b

# CRITIC法
def Critic(M):
    # M是经过Z-score标准化处理后的一个二维数组
    R = np.corrcoef(M)
    R = np.ones(R.shape) - R
    weight = []
    for i, x in enumerate(R):
        u = np.std(M[i]) * sum(x)
        weight.append(u)
    if sum(weight) == 0:
        return np.ones(len(M)) / len(M)
    return abs(np.array(weight)) / sum(abs(np.array(weight)))

# 标准离差法
# 均方差法（针对随机变量）
# mean square error
def MeanError(M):
    weight = []
    for x in M:
        weight.append(np.std(x))
    if sum(weight) == 0:
        return np.ones(len(M)) / len(M)
    return np.array(weight) / sum(np.array(weight))

##可拓权重法
def junior_df(obj):
    # ind_model_cat_id = obj[0].ind_model_cat_id
    dic = json.loads(obj.data)
    df = pd.DataFrame(dic).T
    df.columns = ['period_name', 'evaluator_name', 'senior_index_name', 'junior_index_name', 'value']
    return df

def ExtensionMethod(obj, intervalid,user_id,algorithm_id,ind_model_cat_id,val_model_id):
    junior_index = junior_df(obj)
    junior_index['value'] = (junior_index['value'].values).astype('float64')
    junior_index['junior_index_id'] = junior_index.index
    junior_index['senior_index_id'] = [x[2:4] for x in junior_index['junior_index_id']]
    junior_index['evaluator_id'] = [x[1] for x in junior_index['junior_index_id']]
    junior_index['period_id'] = [x[0] for x in junior_index['junior_index_id']]
    # print(intervalid, type(intervalid))
    # junior_index.to_csv("junior_index.csv", encoding="utf-8")
    for i in junior_index.index:
        junior_index.loc[i, 'intervalid'] = [frozenset(intervalid)]
    # print(junior_index)
    senior_index = junior_index[
        ['period_name', 'evaluator_name', 'senior_index_name', 'intervalid', 'senior_index_id', 'evaluator_id',
         'period_id']]
    senior_index = senior_index.drop_duplicates('senior_index_id')

    e_index = senior_index[['period_name', 'evaluator_name', 'intervalid', 'evaluator_id', 'period_id']]
    e_index = e_index.drop_duplicates(['evaluator_id', 'period_id'])
    p_index = e_index[['period_name', 'intervalid', 'period_id']]
    p_index = p_index.drop_duplicates(['period_id'])

    ###计算可拓权重
    def jdgl(v, intervalid):
        c=0
        if v == intervalid[-1]:
            c = 0.0001
        if v in intervalid:
            v = v + 0.0001
        for i, j in zip(intervalid, intervalid[1:]):
            if v < j:
                if (v - i) < (j - v):
                    c = 2 * (v - i) / (j - i)
                    break
                c = 2 * (j - v) / (j - i)
                break
        return c

    def distance(v, a, b):
        return abs(v - (a + b) / 2) - (b - a) / 2

    # 计算k
    def gl(v, intervalid):
        def distance(v, a, b):
            return abs(v - (a + b) / 2) - (b - a) / 2

        if v == intervalid[-1]:
            v = v - 0.01
        if v in intervalid:
            v = v + 0.01

        def distance(v, a, b):
            return abs(v - (a + b) / 2) - (b - a) / 2

        k = []
        D = distance(v, intervalid[0], intervalid[-1])
        for i, j in zip(intervalid[:-1], intervalid[1:]):
            if v >= i and v < j:
                k.append(distance(v, i, j) / (D - distance(v, i, j) + i - j))
            else:
                if D == distance(v, i, j):
                    k.append((distance(v, i, j) / (i - j)) - 1)
                else:
                    k.append((distance(v, i, j) / (D - distance(v, i, j))))
        maxk = max(k)
        mink = min(k)
        return [(x - mink) / (maxk - mink) for x in k]

    print("sess")
    # print(list(junior_index.loc['000000', 'intervalid'][0]))
    junior_index['weight'] = [jdgl((junior_index.loc[i, 'value']), list(junior_index.loc[i, 'intervalid'][0])) for i in
                              junior_index.index]
    junior_index['k'] = [np.array(gl((junior_index.loc[i, 'value']), list(junior_index.loc[i, 'intervalid'][0]))) for i in
                         junior_index.index]

    ###计算上级指标的值，
    # index_id:上级指标对应的id，
    # intervalid:上级指标对应的经典域，
    # data_frame：下级指标对应的dataframe，
    # col:data_frame中下级指标对应的上级指标的列名

    def index_value(index_id, data_frame, col, intervalid):
        if index_id == '' and col == '':
            df = data_frame
        else:
            df = data_frame[data_frame[col] == index_id]
        if len(df) == 0:
            return 0.0
        if len(df) == 1:
            return df['value'].values[0] * 1.0
        weights = (df['weight'].values) / sum(df['weight'].values)
        k = (weights * df['k']).values[0]
        for i in (weights * df['k']).values[1:]:
            k = k + i
        y = max(k)
        rank = list(k).index(max(k)) + 1
        a = intervalid[rank - 1]
        b = intervalid[rank]
        c = intervalid[0]
        d = intervalid[-1]
        # 将归一化到既有的数值上
        t = ((a - b) / 2) / (abs((a + b) / 2 - (c + d) / 2) + (c - d) / 2 + (b - a) / 2 + a - b)
        y = y * t
        x1 = b + y * (a - d)
        x2 = (b + (a + c) * y) / (1 + 2 * y)
        x3 = (a + (b + d) * y) / (1 + 2 * y)
        x4 = a + y * (b - c)
        l = []
        if x1 >= (a + b) / 2 and x1 >= (c + d) / 2:
            l.append(x1)
        if x2 >= (a + b) / 2 and x2 < +(c + d) / 2:
            l.append(x2)
        if x3 <= (a + b) / 2 and x3 <= (c + d) / 2:
            l.append(x3)
        if x4 <= (a + b) / 2 and x4 <= (c + d) / 2:
            l.append(x4)
        l = [round(x, 2) for x in l]
        if a == c:
            return max(l)
        if b == d:
            return min(l)
        if k[rank] >= k[rank - 2]:
            return max(l)
        if k[rank] < k[rank - 2]:
            return min(l)


    for i in senior_index.index:
        s = list(senior_index.loc[i, 'intervalid'][0])
        print(s)
        senior_index.loc[i, 'value'] = (index_value(senior_index.loc[i, 'senior_index_id'],
                                                    junior_index, 'senior_index_id', s))

    senior_index['weight'] = [jdgl((senior_index.loc[i, 'value']), list(senior_index.loc[i, 'intervalid'][0])) for i in
                              senior_index.index]
    senior_index['k'] = [np.array(gl((senior_index.loc[i, 'value']), list(senior_index.loc[i, 'intervalid'][0]))) for i in
                         senior_index.index]

    for i in e_index.index:
        s = list(e_index.loc[i, 'intervalid'][0])
        e_index.loc[i, 'value'] = (index_value(e_index.loc[i, 'evaluator_id'],
                                               senior_index, 'evaluator_id', s))
    e_index['weight'] = [jdgl((e_index.loc[i, 'value']), list(e_index.loc[i, 'intervalid'][0])) for i in e_index.index]
    e_index['k'] = [np.array(gl((e_index.loc[i, 'value']), list(e_index.loc[i, 'intervalid'][0]))) for i in e_index.index]

    for i in p_index.index:
        s = list(p_index.loc[i, 'intervalid'][0])
        p_index.loc[i, 'value'] = (index_value(p_index.loc[i, 'period_id'],
                                               e_index, 'period_id', s))
    p_index['weight'] = [jdgl((p_index.loc[i, 'value']), list(p_index.loc[i, 'intervalid'][0])) for i in p_index.index]
    p_index['k'] = [np.array(gl((p_index.loc[i, 'value']), list(p_index.loc[i, 'intervalid'][0]))) for i in p_index.index]
    final_score = index_value('', p_index, '', intervalid)
    # print(junior_index)
    # junior_index.to_csv('junior_index.csv')
    # print(senior_index)
    # senior_index.to_csv('senior_index.csv')
    # e_index.to_csv('e_index.csv')
    # p_index.to_csv('p_index.csv')

    # 按评价阶段
    evaluator_index = senior_index[['period_name', 'evaluator_name', 'intervalid', 'evaluator_id', 'period_id']]
    evaluator_index = evaluator_index.drop_duplicates(['evaluator_id'])
    for i in evaluator_index.index:
        s = list(evaluator_index.loc[i, 'intervalid'][0])
        evaluator_index.loc[i, 'value'] = (index_value(evaluator_index.loc[i, 'evaluator_id'],
                                                       senior_index, 'evaluator_id', s))
    evaluator_index['weight'] = [jdgl((evaluator_index.loc[i, 'value']), list(evaluator_index.loc[i, 'intervalid'][0])) for
                                 i in evaluator_index.index]
    evaluator_index['k'] = [np.array(gl((evaluator_index.loc[i, 'value']), list(evaluator_index.loc[i, 'intervalid'][0])))
                            for i in evaluator_index.index]
    e_score = index_value('', evaluator_index, '', intervalid)


    # 按评价阶段
    period_index = senior_index[['period_name', 'intervalid', 'period_id']]
    period_index = period_index.drop_duplicates(['period_id'])
    for i in period_index.index:
        s = list(period_index.loc[i, 'intervalid'][0])
        period_index.loc[i, 'value'] = (index_value(period_index.loc[i, 'period_id'],
                                                    senior_index, 'period_id', s))
    period_index['weight'] = [jdgl((period_index.loc[i, 'value']), list(period_index.loc[i, 'intervalid'][0])) for i in
                              period_index.index]
    period_index['k'] = [np.array(gl((period_index.loc[i, 'value']), list(period_index.loc[i, 'intervalid'][0]))) for i in
                         period_index.index]
    p_score = index_value('', period_index, '', intervalid)

    # -*- coding: utf-8 -*-
    def senior_detail_plot(senior_index,junior_index):
        name_list = senior_index['senior_index_id']
        num_list = senior_index['value']
        name = list(senior_index['senior_index_name'].values)
        for i in range(len(name_list)):
            name[i] = name_list[i] + name[i]

        def f(s):
            string = s[0]
            for i in s[1:-1]:
                string = string + i + '\n'
            return string + s[-1]

        name = [f(x) for x in name]
        plt.figure(figsize=(16, 8))
        plt.bar(range(len(num_list)), num_list, color='rgbycm', tick_label=name)
        plt.title("一级指标量值表", fontsize=25)
        plt.xlabel('一级指标', fontsize=20)
        plt.ylabel('指标值', fontsize=20)
        for a, b in zip(range(len(num_list)), num_list):
            plt.text(a, b + 0.05, '%3.1f' % b, ha='center', va='bottom', fontsize=13)
        plt.xticks(fontsize=15)  # ,rotation='vertical')
        plt.yticks(fontsize=15)
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        return data



    ##查看一级指标值
    def index_plot(df, t, score):
        s=''
        if t == 0:
            title = '按评价者计算' + ':' + str(score)
            s = 'evaluator_name'
        if t == 1:
            title = '按评价阶段计算' + ':' + str(score)
            s = 'period_name'
        plt.figure(figsize=(6, 9))
        labels = df[s].values
        labels1 = []
        s = df['value'].values
        for i in range(len(labels)):
            labels1.append(labels[i] + ':' + str(s[i]))
        sizes = df['value']
        explode = None
        plt.pie(sizes, explode=explode, labels=labels1,
                labeldistance=1.1, shadow=False, startangle=90, textprops={'fontsize': 15})
        plt.title(title, fontsize=20)
        plt.axis('equal')
        plt.legend(labels, fontsize=10)
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        return data

    senior_detail_plot = senior_detail_plot(senior_index,junior_index)
    evaluator_plot = index_plot(evaluator_index, 0, e_score)
    period_plot = index_plot(period_index, 1, p_score)

    junior_index = junior_index.to_json(orient='index')
    senior_index = senior_index.to_json()
    evaluator_index = evaluator_index.to_json()
    period_index = period_index.to_json()
    p_index = p_index.to_json()

    # print(len(obj))

    now = datetime.datetime.now()  # 时间
    now_str = now.strftime('%Y%m%d%H%M%S%f')
    val_res_id = user_id + now_str  # 建立val_res_id,加入毫秒，防止重复
    print(val_res_id)

    models.val_res.objects.create(val_res_id=val_res_id, final_res=final_score, period_res=period_index,
                                  evaluator_res=evaluator_index, senior_res=senior_index,
                                  e_res=e_score, p_res=p_score, junior_res=junior_index,
                                  p_index_res=p_index, val_model_id=val_model_id,
                                  user_id_id=user_id, ind_model_cat_id=ind_model_cat_id,
                                  algorithm_id_id=algorithm_id, company_id_id=obj.company_id_id,
                                  senior_detail_plot=senior_detail_plot, evaluator_plot=evaluator_plot,
                                  period_plot=period_plot)

    return 'ok'