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
    secondary_data = pd.DataFrame(['南京市', '苏州市', '无锡市', '常州市', '镇江市', '南通市', '连云港市',
                                   '淮安市', '泰州市', '徐州市', '盐城市', '扬州市', '宿迁市'], columns=['city'])
    # print(secondary_data)
    for i in range(12):
        secondary_data_i = data.iloc[[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [1+2*i, 2+2*i]]
        secondary_data_i.columns = ['city', secondary_indicators[i]]
        secondary_data = pd.merge(secondary_data, secondary_data_i, how='left', on='city')
    # print(secondary_data)
    """一级指标数据处理"""
    primary_indicators = list(data.iloc[16].dropna())[1:6]
    # print(primary_indicators)
    primary_data = pd.DataFrame(['南京市', '苏州市', '无锡市', '常州市', '镇江市', '南通市', '连云港市',
                                '淮安市', '泰州市', '徐州市', '盐城市', '扬州市', '宿迁市'], columns=['city'])
    for i in range(5):
        primary_data_i = data.iloc[[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [1+2*i, 2+2*i]]
        primary_data_i.columns = ['city', primary_indicators[i]]
        primary_data = pd.merge(primary_data, primary_data_i, how='left', on='city')
    """总得分"""
    city = pd.DataFrame(['南京市', '苏州市', '无锡市', '常州市', '镇江市', '南通市', '连云港市',
                        '淮安市', '泰州市', '徐州市', '盐城市', '扬州市', '宿迁市'], columns=['city'])
    total_data = data.iloc[[18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, ], [12, 13]]
    total_data.columns = ['city', 'score']
    total_data = pd.merge(city, total_data, how='left', on='city')
    return secondary_data, primary_data, total_data


def chart(database):
    page = Page(page_title=str(database[0][1])+'方法')
    configure(global_theme='essos')
    n = len(database)
    style = dict(
        is_datazoom_show=True,
        datazoom_range=[0,100],
        xaxis_type='category',
        is_xaxislabel_align=True,
        xaxis_rotate=15,
        xaxis_label_textsize=16,
        yaxis_label_textsize=16,
        xaxis_name_size=20,
        yaxis_name_size=20,
        xaxis_name='指标名',
        yaxis_name='得分',
        legend_pos='right',
        legend_top='3%',
        xaxis_name_pos='end',
        is_label_show =True,
    )
    style2 = dict(
        is_datazoom_show=True,
        datazoom_range=[0, 100],
        xaxis_type='category',
        is_xaxislabel_align=True,
        xaxis_label_textsize=16,
        yaxis_label_textsize=16,
        xaxis_name_size=20,
        yaxis_name_size=20,
        xaxis_name='指标名',
        yaxis_name='得分',
        legend_pos='right',
        legend_top='3%',
        xaxis_name_pos='end',
        is_label_show=True,
    )
    style3 = dict(
        is_datazoom_show=True,
        datazoom_range=[0, 100],
        xaxis_type='category',
        is_xaxislabel_align=True,
        xaxis_label_textsize=16,
        yaxis_label_textsize=16,
        xaxis_name_size=20,
        yaxis_name_size=20,
        xaxis_name='城市',
        yaxis_name='得分',
        legend_pos='right',
        legend_top='3%',
        xaxis_name_pos='end',
        is_label_show=True,
    )
    timeline1 = Timeline(is_auto_play=True, timeline_bottom=20, width=1500, height=700, is_loop_play=False, )
    timeline2 = Timeline(is_auto_play=True, timeline_bottom=20, width=1500, height=700, is_loop_play=False, )
    timeline3 = Timeline(is_auto_play=True, timeline_bottom=20, width=1500, height=700, is_loop_play=False, )
    for i in range(n):
        year = database[i][0]
        name = database[i][1]
        title1 =str(year)+'年各城市二级指标得分情况'+'\n\n\n'
        li = database[i][2]['city']
        secondary_indicators = database[i][2].columns.tolist()[1:]
        grid = Grid()
        bar_1 = Bar(title1, title_text_size=28, title_pos='auto')
        bar_1.add(li[0], secondary_indicators, database[i][2].iloc[0].values[1:], **style)
        bar_1.add(li[1], secondary_indicators, database[i][2].iloc[1].values[1:], **style)
        bar_1.add(li[2], secondary_indicators, database[i][2].iloc[2].values[1:], **style)
        bar_1.add(li[3], secondary_indicators, database[i][2].iloc[3].values[1:], **style)
        bar_1.add(li[4], secondary_indicators, database[i][2].iloc[4].values[1:], **style)
        bar_1.add(li[5], secondary_indicators, database[i][2].iloc[5].values[1:], **style)
        bar_1.add(li[6], secondary_indicators, database[i][2].iloc[6].values[1:], **style)
        bar_1.add(li[7], secondary_indicators, database[i][2].iloc[7].values[1:], **style)
        bar_1.add(li[8], secondary_indicators, database[i][2].iloc[8].values[1:], **style)
        bar_1.add(li[9], secondary_indicators, database[i][2].iloc[9].values[1:], **style)
        bar_1.add(li[10], secondary_indicators,database[i][2].iloc[10].values[1:], **style)
        bar_1.add(li[11], secondary_indicators, database[i][2].iloc[11].values[1:], **style)
        bar_1.add(li[12], secondary_indicators, database[i][2].iloc[12].values[1:], **style)
        grid.add(bar_1,grid_top='10%',grid_bottom='15%')
        timeline1.add(grid, str(year)+'年数据')

        title2 = str(year)+'年各城市一级指标得分情况'
        primary_indicators = database[i][3].columns.tolist()[1:]
        grid2 = Grid()
        bar_2 = Bar(title2, title_text_size=28, title_pos='auto', )
        bar_2.add(li[0], primary_indicators, database[i][3].iloc[0].values[1:], **style2)
        bar_2.add(li[1], primary_indicators, database[i][3].iloc[1].values[1:], **style2)
        bar_2.add(li[2], primary_indicators, database[i][3].iloc[2].values[1:], **style2)
        bar_2.add(li[3], primary_indicators, database[i][3].iloc[3].values[1:], **style2)
        bar_2.add(li[4], primary_indicators, database[i][3].iloc[4].values[1:], **style2)
        bar_2.add(li[5], primary_indicators, database[i][3].iloc[5].values[1:], **style2)
        bar_2.add(li[6], primary_indicators, database[i][3].iloc[6].values[1:], **style2)
        bar_2.add(li[7], primary_indicators, database[i][3].iloc[7].values[1:], **style2)
        bar_2.add(li[8], primary_indicators, database[i][3].iloc[8].values[1:], **style2)
        bar_2.add(li[9], primary_indicators, database[i][3].iloc[9].values[1:], **style2)
        bar_2.add(li[10], primary_indicators, database[i][3].iloc[10].values[1:], **style2)
        bar_2.add(li[11], primary_indicators, database[i][3].iloc[11].values[1:], **style2)
        bar_2.add(li[12], primary_indicators, database[i][3].iloc[12].values[1:], **style2)
        grid2.add(bar_2,grid_bottom='15%')
        timeline2.add(grid2, str(year) + '年数据')

        grid3 =Grid()
        title3 = str(year) + '年各城市总得分情况'
        total_score = database[i][4]['score'].values
        bar_3 = Bar(title3, title_text_size=28, title_pos='auto', )
        bar_3.add("各城市总得分",li, total_score, **style3)
        grid3.add(bar_3, grid_bottom='15%')
        timeline3.add(grid3, str(year) + '年数据')

    # timeline2.render()
    page.add_chart(timeline1)
    page.add_chart(timeline2)
    page.add_chart(timeline3)
    page.render(str(database[0][1])+'.html')

#
# def schartsec(secondary_indicators, secondary_data_16, secondary_data_17):
#     configure(global_theme='essos')
#     bar_1 = Bar('topisis方法:2017年各城市二级指标得分情况', title_text_size=28, title_pos='auto', )
#     style = dict(
#         xaxis_name_size=24,
#         yaxis_name_size=24,
#         xaxis_name='二级指标',
#         yaxis_name='得分',
#         legend_pos='right',
#         # legend_top='center'
#         xaxis_name_pos='end'
#     )
#
#     bar_1.add('南京市', secondary_indicators, secondary_data_17[0], **style)
#     bar_1.add('苏州市', secondary_indicators, secondary_data_17[1], **style)
#     bar_1.add('常州市', secondary_indicators, secondary_data_17[2], **style)
#     bar_1.add('无锡市', secondary_indicators, secondary_data_17[3], **style)
#     bar_1.add('徐州市', secondary_indicators, secondary_data_17[4], **style)
#     bar_1.add('连云港市', secondary_indicators, secondary_data_17[5], **style)
#     bar_1.add('泰州市', secondary_indicators, secondary_data_17[6], **style)
#     bar_1.add('扬州市', secondary_indicators, secondary_data_17[7], **style)
#     bar_1.add('宿迁市', secondary_indicators, secondary_data_17[8], **style)
#     bar_1.add('镇江市', secondary_indicators, secondary_data_17[9], **style)
#     bar_1.add('盐城市', secondary_indicators, secondary_data_17[10], **style)
#     bar_1.add('南通市', secondary_indicators, secondary_data_17[11], **style)
#     bar_1.add('淮安市', secondary_indicators, secondary_data_17[12], **style)
#
#     bar_2 = Bar('topisis方法:2016年各城市二级指标得分情况', title_text_size=28, title_pos='auto', )
#     bar_2.add('南京市', secondary_indicators, secondary_data_16[0], **style)
#     bar_2.add('苏州市', secondary_indicators, secondary_data_16[1], **style)
#     bar_2.add('常州市', secondary_indicators, secondary_data_16[2], **style)
#     bar_2.add('无锡市', secondary_indicators, secondary_data_16[3], **style)
#     bar_2.add('徐州市', secondary_indicators, secondary_data_16[4], **style)
#     bar_2.add('连云港市', secondary_indicators, secondary_data_16[5], **style)
#     bar_2.add('泰州市', secondary_indicators, secondary_data_16[6], **style)
#     bar_2.add('扬州市', secondary_indicators, secondary_data_16[7], **style)
#     bar_2.add('宿迁市', secondary_indicators, secondary_data_16[8], **style)
#     bar_2.add('镇江市', secondary_indicators, secondary_data_16[9], **style)
#     bar_2.add('盐城市', secondary_indicators, secondary_data_16[10], **style)
#     bar_2.add('南通市', secondary_indicators, secondary_data_16[11], **style)
#     bar_2.add('淮安市', secondary_indicators, secondary_data_16[12], **style)
#     timeline = Timeline(is_auto_play=True, timeline_bottom=0, width=1600, height=700, is_loop_play=False, )
#     timeline.timeline_top = 20
#     timeline.add(bar_2, '2016年')
#     timeline.add(bar_1, '2017年')
#
#     timeline.render('topisis方法,2016-2017年各城市二级指标得分情况.html')
#
#
# def pchartpri(primary_indicators, primary_data_16, primary_data_17):
#     configure(global_theme='shine')
#     bar_1 = Bar('topisis方法:2016年各城市一级指标得分情况', title_text_size=28, title_pos='auto', )
#     style = dict(
#         xaxis_name_size=24,
#         yaxis_name_size=24,
#         xaxis_name='一级指标',
#         yaxis_name='得分',
#         legend_pos='right',
#         # legend_top='center'
#         xaxis_name_pos='end'
#     )
#     bar_1.add('南京市', primary_indicators, primary_data_16[0], **style)
#     bar_1.add('苏州市', primary_indicators, primary_data_16[1], **style)
#     bar_1.add('常州市', primary_indicators, primary_data_16[2], **style)
#     bar_1.add('无锡市', primary_indicators, primary_data_16[3], **style)
#     bar_1.add('徐州市', primary_indicators, primary_data_16[4], **style)
#     bar_1.add('连云港市', primary_indicators, primary_data_16[5], **style)
#     bar_1.add('泰州市', primary_indicators, primary_data_16[6], **style)
#     bar_1.add('扬州市', primary_indicators, primary_data_16[7], **style)
#     bar_1.add('宿迁市', primary_indicators, primary_data_16[8], **style)
#     bar_1.add('镇江市', primary_indicators, primary_data_16[9], **style)
#     bar_1.add('盐城市', primary_indicators, primary_data_16[10], **style)
#     bar_1.add('南通市', primary_indicators, primary_data_16[11], **style)
#     bar_1.add('淮安市', primary_indicators, primary_data_16[12], **style)
#
#     bar_2 = Bar('topisis方法:2017年各城市二级指标得分情况', title_text_size=28, title_pos='auto', )
#     bar_2.add('南京市', primary_indicators, primary_data_17[0], **style)
#     bar_2.add('苏州市', primary_indicators, primary_data_17[1], **style)
#     bar_2.add('常州市', primary_indicators, primary_data_17[2], **style)
#     bar_2.add('无锡市', primary_indicators, primary_data_17[3], **style)
#     bar_2.add('徐州市', primary_indicators, primary_data_17[4], **style)
#     bar_2.add('连云港市', primary_indicators, primary_data_17[5], **style)
#     bar_2.add('泰州市', primary_indicators, primary_data_17[6], **style)
#     bar_2.add('扬州市', primary_indicators, primary_data_17[7], **style)
#     bar_2.add('宿迁市', primary_indicators, primary_data_17[8], **style)
#     bar_2.add('镇江市', primary_indicators, primary_data_17[9], **style)
#     bar_2.add('盐城市', primary_indicators, primary_data_17[10], **style)
#     bar_2.add('南通市', primary_indicators, primary_data_17[11], **style)
#     bar_2.add('淮安市', primary_indicators, primary_data_17[12], **style)
#     timeline = Timeline(is_auto_play=True, timeline_bottom=0, width=1600, height=700, is_loop_play=False, )
#     timeline.timeline_top = 20
#     timeline.add(bar_2, '2016年')
#     timeline.add(bar_1, '2017年')
#
#     timeline.render('topisis方法,2016-2017年各城市一级指标得分情况.html')
#
#
# def totalchart(total_score_16, total_score_17):
#     configure(global_theme='shine')
#     bar_1 = Bar('topisis方法:2016年各城市总得分', title_text_size=28, title_pos='auto', )
#     style = dict(
#         xaxis_name_size=24,
#         yaxis_name_size=24,
#         xaxis_name='城市',
#         yaxis_name='得分',
#         legend_pos='right',
#         # legend_top='center'
#         xaxis_name_pos='end'
#     )
#     attr = ['苏州市', '南京市', '无锡市', '常州市', '泰州市', '连云港市', '南通市',
#             '徐州市', '宿迁市', '淮安市', '盐城市', '镇江市', '扬州市']
#     v1 = list(total_score_16)
#     v2 = list(total_score_17)
#     bar_1.add("各城市总得分", attr, v1, **style)
#     bar_2 = Bar('topisis方法:2017年各城市总得分', title_text_size=28, title_pos='auto', )
#     bar_2.add("各城市总得分", attr, v2, **style)
#     timeline = Timeline(is_auto_play=True, timeline_bottom=0, width=1600, height=700, is_loop_play=False, )
#     timeline.timeline_top = 20
#     timeline.add(bar_1, '2016年')
#     timeline.add(bar_2, '2017年')
#
#     timeline.render('topisis方法,2016-2017年各城市评价总得分情况.html')


if __name__ == '__main__':
    load()
    # secondary_indicators, secondary_data_16, secondary_data_17 = loadsec()
    # Schartsec(secondary_indicators, secondary_data_16, secondary_data_17)
    # primary_indicators,primary_data_16,primary_data_17 = loadpri()
    # Pchartpri(primary_indicators,primary_data_16,primary_data_17)
