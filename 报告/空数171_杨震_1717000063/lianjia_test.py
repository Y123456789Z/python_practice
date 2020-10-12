# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:48:17 2020

@author: lenovo
"""

import numpy as npy
import pandas as pda
data=pda.read_csv("lianjia.csv")
select_data=data
print(select_data)
print('**********************')
print('第一问')
unknow_Construction_time=select_data.loc[(select_data['Construction time'].isin(['未知']))]
print(unknow_Construction_time)
print('**********************')
print('第二问')
sale_money=select_data[~(select_data['Construction time'].isin(['未知','0','1']))]
sort_sale=sale_money.sort_values('Construction time').head(1)[['Total price',
                                'Construction time']]
print(sort_sale)
print('**********************')
print('第三问')
wooden_price=data.loc[(data['District'].isin(['海淀']))]
mean_price=wooden_price['Price'].mean()
print(round(mean_price,2))
print('**********************')
print('第四问')
two_live_house_count=data[data['District'].isin(['西城'])&data['Bed Room']
.isin([2])]
print(len(two_live_house_count))
print('**********************')
print('第五问')
wooden_message=data[data['Square']>100]
print(wooden_message)