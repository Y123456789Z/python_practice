# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 09:39:00 2018

@author: Administrator
"""

from selenium import webdriver         #selenium请求库是自动化测试工具，可以驱动浏览器自动执行自定义好的逻辑代码，也就是
#可以通过代码完全模拟成人类使用浏览器自动访问目标站点并操作     
from bs4 import BeautifulSoup
import time
import csv
import re

titles,prices,shops,sales,appraise = [],[],[],[],[]

#csvFile = open("ydzhuang_women.csv","w",newline='') # newline=''解决空白行问题
csvFile = open("ydzhuang_men.csv","w",newline='')
writer = csv.writer(csvFile)
writer.writerow(('title','price','shop','sale','appraise'))

def getInfo(page):
    
#   url_women ="https://re.taobao.com/search?refpid=420435_1006&keyword=%E8%BF%90%E5%8A%A8%E8%A3%85++%E5%A5%B3&_input_charset=utf-8&page=" +str(page)+"&isinner=0&rewriteKeyword"
    url_men = "https://re.taobao.com/search?refpid=420435_1006&keyword=%E8%BF%90%E5%8A%A8%E8%A3%85+%E7%94%B7&_input_charset=utf-8&page="+str(page)+"&isinner=0&rewriteKeyword"
    
    #配置headless
    ChromeOptions = webdriver.ChromeOptions()
    ChromeOptions.set_headless() #设置为headless模式   这个模式下，我们可以不打开浏览器爬取数据
    driver = webdriver.Chrome(chrome_options=ChromeOptions)
    time.sleep(3)   #推迟调用线程的运行，2表示进程挂起的时间，休眠2秒
#    driver.get(url_women)
    driver.get(url_men) #得到网页源代码
    
    soup = BeautifulSoup(driver.page_source, 'html.parser') #利用beautifulsoup ,解析网页代码结构，获得需要爬取的元素
    titles = soup.findAll('span',class_='title')
    prices = soup.findAll('span',class_='pricedetail')
    shops = soup.findAll('span',class_='shopNick')
    sales = soup.findAll('span',class_='payNum')
    appraise = soup.findAll('span',class_='dsr-info-num')
    print(len(titles))
    for i in range(len(titles)):
        saleNum = re.findall(r"\d+\.?\d*",sales[i].get_text()) #提取销售数量数值，正则表达式提取需要的东西
        writer.writerow((titles[i].get_text(),prices[i].find('strong').get_text(),shops[i].get_text(),''.join(saleNum),appraise[i].get_text()))
        
    driver.quit() # 表示关闭浏览器

for page in range(0,50): # 爬取前10页
    print ("正在爬取第{}页".format(page))
    getInfo(page)

csvFile.close() # 关闭文件
print("完成！")