# -*- coding: utf-8 -*-
# author:xls
"""
    @property装饰器：把类的方法伪装成属性调用的方式
"""

class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @age.deleter
    def age(self):
        print("删除年龄数据！")

obj = People("jack", 18)
print(obj.age)
obj.age = 19
print("obj.age:  ", obj.age)
del obj.age
