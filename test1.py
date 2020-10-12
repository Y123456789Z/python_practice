# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:08:35 2020

@author: lenovo
"""

#for j in range(1,10):
#    for i in range(1,j+1):
#        print("{}*{}={}".format(i,j,i*j),end=" ")
#    print(" ")
#print("\n")
#a=float(input("边长一："))
#b=float(input("边长二："))
#c=float(input("边长三："))
#s=(a+b+c)/2
#area=(s*(s-a)*(s-b)*(s-c))**0.5
#print("面积为：%0.2f" %area)
#print("\n")
#string_1=input("输入内容：")
#print("小写",string_1.lower())
#print("大写：",string_1.upper())
#class singer(object):
#    name="a"
#    def way1(self):
#        print("a12")
#class sportor(object):
#    name="b"
#    def way2(self):
#        print("b12")
#
#class dxs(object,singer,sportor):
#    name="c"
#    def way3(self):
#        print("c12")


#class dog:
#    cute_name="小黑"
#    jiankang_value="89"
#    
#    def animate(self):
#        print("摇尾巴")
#class cat:
#    cute_name="小白"
#    jiankang_value="99"
#   
#    def animate(self):
#        print("上树")
#class panguim:
#    cute_name="小Q"
#    jiankang_value="98"
#    
#    def animate(self):
#        print("潜水")
#class animal(dog,cat,panguim):
#    def qinmi(self):
#        print("{}和主人亲密，健康值是{}".format(dog.cute_name,dog.jiankang_value))


class animal:
    cute_name=""
    jiankang_value=""
    
    def __init__(self,a,b):
        self.cute_name=a
        self.jiankang_value=b
    def animate(self):
        print("昵称是{}，健康值是{}".format(self.cute_name,self.jiankang_value))
class dog(animal):
    animal_class="" 
    def __init__(self,a,b,c):
        self.cute_name=a
        self.jiankang_value=b
        self.animal_class=c
    def animate(self):
        print("{}和主人亲密，昵称是{}，健康值是{}".format(self.animal_class,self.cute_name,self.jiankang_value))
class cat(animal):
    animal_class="" 
    def __init__(self,a,b,d):
        self.cute_name=a
        self.jiankang_value=b
        self.animal_class=d
    def animate(self):
        print("{}和主人亲密，昵称是{}，健康值是{}".format(self.animal_class,self.cute_name,self.jiankang_value))      
class panguim(animal):
    animal_class="" 
    def __init__(self,a,b,e):
        self.cute_name=a
        self.jiankang_value=b
        self.animal_class=e
    def animate(self):
        print("{}和主人亲密，昵称是{}，健康值是{}".format(self.animal_class,self.cute_name,self.jiankang_value))       
m=dog("小黑","89","狗")
m.animate()
n=cat("小白","99","猫")
n.animate()
p=panguim("小Q","87","企鹅")
p.animate()
    

