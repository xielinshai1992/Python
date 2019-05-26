# -*- coding: utf-8 -*-
# author:xls
"""
    递归和迭代实现阶乘
"""
def factorial_1(n):
    '''
    递归实现阶乘
    :param n:
    :return:
    '''
    if n==1:
        return 1
    else:
        return n*factorial_1(n-1)


def factorial_2(n):
    '''
    迭代实现阶乘
    :param n:
    :return:
    '''
    result =n
    for i in range(1,n):
        result*=i
    return result

number =int(input('请输入一个正整数:'))
print(factorial_1(number))
