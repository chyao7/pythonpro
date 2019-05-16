from pyecharts import Bar, Timeline
import pandas as pd
import re
import numpy as np
from pyecharts import configure
import os
from pyecharts import Bar, Line, Overlap
from pyecharts import Page,Grid


def load():
    """
    载入 数据
    """
    files = os.listdir('./')
    topis = []
    composite_index = []
    for file in files:
        r = re.findall('(\w+)_(\d+)',file)
        if r:
            if r[0][0]=='topsis':
                print(file)
                data = pd.read_excel(file)
                topis_secondary_data, topis_primary_data, topis_total_data = dataprocewss(data)
                topis.append([r[0][1],r[0][0],topis_secondary_data, topis_primary_data, topis_total_data])
            if r[0][0] == '综合指数法':
                # print(file)
                data = pd.read_excel(file)
                composite_index_secondary_data, composite_index_primary_data, composite_index_total_data = dataprocewss(data)
                composite_index.append([r[0][1],r[0][0], composite_index_secondary_data, composite_index_primary_data, composite_index_total_data])
        else:
            pass
    chart(topis)
    chart(composite_index)


def dataprocewss(data):
    """
数据处理
    :param data:原始数据
    """
    """二级指标数据"""
    secondary_indicators = list(data.iloc[0].dropna())[1:]
    # print(secondary_data)
    secondary_data=[]
    for i in range(12):
        secondary_data.append(data.iloc[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [1+2*i, 2+2*i]])
        secondary_data[i].columns = ['city', secondary_indicators[i]]
    # print(secondary_data[0])
    # print(secondary_data)
    """一级指标数据处理"""
    primary_indicators = list(data.iloc[16].dropna())[1:6]
    # print(primary_indicators)
    primary_data = []
    for i in range(5):
        primary_data.append(data.iloc[[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [1+2*i, 2+2*i]])
        primary_data[i].columns = ['city', primary_indicators[i]]
    """总得分"""
    city = pd.DataFrame(['南京市', '苏州市', '无锡市', '常州市', '镇江市', '南通市', '连云港市',
                        '淮安市', '泰州市', '徐州市', '盐城市', '扬州市', '宿迁市'], columns=['city'])
    total_data = data.iloc[[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, ], [12, 13]]
    total_data.columns = ['city', 'score']
    total_data = pd.merge(city, total_data, how='left', on='city')
    return secondary_data, primary_data, total_data


def chart(database):

    # configure(global_theme='essos')
    n = len(database)
    style = dict(
        xaxis_type='category',
        is_xaxislabel_align=True,
        xaxis_rotate=90,
        xaxis_label_textsize=16,
        yaxis_label_textsize=16,
        xaxis_name_size=20,
        yaxis_name_size=20,
        xaxis_name='城市',
        yaxis_name='得分',
        legend_pos='right',
        legend_top='3%',
        xaxis_name_pos='end',
        is_label_show =True,
        mark_line=['average'],
        mark_point=['min','max']
    )
    # timeline1 = Timeline(is_auto_play=True, timeline_bottom=20, width=1500, height=700, is_loop_play=False, )
    # timeline2 = Timeline(is_auto_play=True, timeline_bottom=20, width=1500, height=700, is_loop_play=False, )
    # timeline3 = Timeline(is_auto_play=True, timeline_bottom=20, width=1500, height=700, is_loop_play=False, )
    # grid = Grid(height=400)
    for i in range(n):
        year = database[i][0]
        name = database[i][1]
        title1 =name+str(year)+'年各城市二级指标得分情况'
        page = Page(title1)
        # li = database[i][2]['city']
        for j in database[i][2]:
            column = j.columns.tolist()[1]
            x = j.sort_values(by=column,ascending=False)
            print(x)
            bar = Bar(column,height=500,width=1300,)
            bar.add(column,x['city'].values.tolist(),x[column].values.tolist(),**style)
            page.add(bar)
        page.render(title1+'.html')

        title2 = name + str(year) + '年各城市一级指标得分情况'
        page2 = Page(title2)
        for j in database[i][3]:
            column = j.columns.tolist()[1]
            x = j.sort_values(by=column, ascending=False)
            bar = Bar(column, height=500, width=1300, )
            bar.add(column, x['city'].values.tolist(), x[column].values.tolist(), **style)
            page2.add(bar)
        page2.render(title2 + '.html')

        title3 = name + str(year) + '年各城市评价总得分情况'
        x_total = database[i][4].sort_values(by='score',ascending=False)

        bar_total = Bar(title3,height=700,width=1300)
        bar_total.add('各城市总得分',x_total['city'].values.tolist(),
                      x_total.values.tolist(),**style)
        bar_total.render(title3 + '.html')



if __name__ == '__main__':
    load()
    # secondary_indicators, secondary_data_16, secondary_data_17 = loadsec()
    # Schartsec(secondary_indicators, secondary_data_16, secondary_data_17)
    # primary_indicators,primary_data_16,primary_data_17 = loadpri()
    # Pchartpri(primary_indicators,primary_data_16,primary_data_17)
