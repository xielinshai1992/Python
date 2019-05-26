# -*- coding: utf-8 -*-
# author:xls
"""
    # python3的继承机制  多继承
    # 子类在调用某个方法或变量的时候，首先在自己内部查找，如果没有找到，则开始根据继承机制在父类里查找。
    # 根据父类定义中的顺序，以深度优先（写在前面的父类优先继承）的方式逐一查找父类！
"""

class people:
    '''
    父类定义
    '''
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

class student(people):
    '''
    # 单继承示例
    '''
    def __init__(self, name, age, weight, grade):
        # 调用父类的实例化方法
        people.__init__(self, name, age, weight)
        self.grade = grade

    # 重写父类的speak方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

s = student('ken', 10, 30, 3)
s.speak()