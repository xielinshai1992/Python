# -*- coding: utf-8 -*-
# author:xls
"""
    pickle:Python专用的持久化模块
"""
import pickle

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)

a = Person('jack',20)
a.show()
with open(r'd:\1.pickle','wb') as f:
    pickle.dump(a,f)      #将Python数据转换并保存到pickle格式的文件内

# with open(r'd:\1.pickle','rb') as f:
#     b = pickle.load(f)    #从pickle格式的文件中读取数据并转换为python的类型
# print(b)
# b.show()