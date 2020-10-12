import numpy as npy
import pandas as pda
data1=pda.read_csv('brand.csv')
data2=pda.read_csv('guazi_sec_car.csv')
data2['brand']=0
data2.to_csv('new_guazi_sec_car.csv')
print(data2.columns)
def str_than(str1,str2):
    if str1 in str2:
        return 1
    else:
        return 2
for item,col in enumerate(data2['full_name']):
    for element in data1['brand']:
        if str_than(element,col)==1:
            data2.iloc[item,5]=element
data2.to_csv('new_guazi_sec_car.csv')
print('新建列完成！')
