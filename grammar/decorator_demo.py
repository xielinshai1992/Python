# -*- coding: utf-8 -*-
# author:xls
"""
    装饰器demo
"""
def outer(func):
    def inner():
        print("认证成功！")
        result = func()
        print("日志添加成功")
        return result
    return inner

@outer
def f1():
    print("业务部门1数据接口......")

@outer
def f2():
    print("业务部门2数据接口......")

@outer
def f3():
    print("业务部门3数据接口......")

@outer
def f100():
    print("业务部门100数据接口......")

#各部门分别调用
f1()
f2()
f3()
f100()