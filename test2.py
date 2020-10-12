# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:21:21 2020

@author: lenovo
"""
"""正则表达式"""
#import re
#print(re.match("www","www.runoob.com").span())
#print(re.match("com","www.runoob.com"))
#import pandas as pda
#data1=pda.Series([1,2,3,4])
#data2=pda.Series([5,6,7,8])
#data3=pda.Series(["abc","bda"])
#data4=pda.Series(["c","d"])
#compare1=data1>data2
#print(compare1)
#compare2=data3>data4
#print(compare2)
#search1=data3.str.endswith('c')
#
"""pandas"""
#print(search1)
#search2=data3.str.len()
#print(search2)
#import pandas as pda
#data1=pda.Series([1,2,2,3,5,5])
#sort1=data1.value_counts(ascending=False)
#print(sort1)
#sort2=sort1.head(2)
"""dataframe"""
#import numpy as npy
#import pandas as pda
#"""iloc是名称索引，loc是数字索引"""
#data=pda.DataFrame({'type':['坦克','射手','射手','刺客'],'name':['张飞','后羿','鲁班','李白']
#,'生命值':['100','123','342','134']},index=['a','b','c','d'])
#print(data)
##data1=data.groupby('type').count()['name']
##print(data1)
##data2=data.sort_values('生命值',ascending=False).head(1)
##data3=data.sort_values('生命值',ascending=False).tail(1)
##print(data2)
##print(data3)
#data4=data.loc['a']

'''表连接'''


'''王者数据分析'''
#一共多少英雄
#每个英雄有多少个属性
#找到所有英雄血量最多的英雄
#获得每一种英雄的平均属性（取两位小数）
#查找远程、近程英雄的数量
#英雄生命恢复的排行榜前十个
#使用reindex重新为生命恢复排行榜设置索引
#import numpy as npy
#import pandas as pda
#data=pda.read_csv('type_hero.csv')

#print(len(file.))
#
#
#print(len(file.columns[1])-2)
#data.reset_index(drop=True).set_index(append=True)
"""链家"""
#import numpy as npy
#import pandas as pda
#data=pda.read_csv("lianjia.csv")
#select_data=data
#print(select_data)
#print('**********************')
#unknow_Construction_time=select_data.loc[(select_data['Construction time'].isin(['未知']))]
#print(unknow_Construction_time)
#print('**********************')
#sale_money=select_data[~(select_data['Construction time'].isin(['未知','0','1']))]
#sort_sale=sale_money.sort_values('Construction time').head(1)[['Total price',
#                                'Construction time']]
#print(sort_sale)
#print('**********************')
#wooden_price=data.loc[(data['District'].isin(['海淀']))]
#mean_price=wooden_price['Price'].mean()
#print(round(mean_price,2))
#print('**********************')
#two_live_house_count=data[data['District'].isin(['西城'])&data['Bed Room']
#.isin([2])]
#print(len(two_live_house_count))
#print('**********************')
#wooden_message=data[data['Square']>100]
#print(wooden_message)
#import pandas as pda
#import numpy as npy
#data=pda.Series(['yz','dhf','dshf','dff','fe','fgfg'])
#print(data[1])
#print(data.head(2))
#print(data.tail(2))
#print(data.sort_values(ascending=False))
#data.reset_index(drop=True)
#print(data)
#import numpy as npy
#import pandas as pda
#data=pda.DataFrame({'1':['df','dfs'],'2':['we','dgg']})
'''爬虫'''
#通过数据接口爬取
#import requests as req
#
#import time as ti
#import csv as cs
#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
#response=req.get('https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0',headers=headers)
#if response.status_code==200:
#    print(response.text)
#    data=response.json()
#通过html爬取
'''二手车'''
#增加品牌列
#汽车使用年限保值率，1-5年
#每个品牌目前在市场的保有量
#公里数与价格关系
##同年品牌不同配置的保值率
import numpy as npy
import pandas as pda
data1=pda.read_csv('guazi_sec_car.csv')
data2=pda.read_csv('brand.csv')
brand_data=data2['brand']
name=data1['full_name']
print(name)
for item in range(len(name)):
    split_name=data1[item].split(' ')
    print(split_name)
#for item in brand_data:
#    for element in name:
#        if brand_data[item] in name[element]:
#            print("yes")















