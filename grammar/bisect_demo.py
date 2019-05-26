# -*- coding: utf-8 -*-
# author:xls
"""
    bisect模块实现二分查找和插入算法.
"""
import bisect

x1= 200
x2= 500
list1 = [1, 3, 6, 24, 55, 78, 454, 555, 1234, 6900]
list2 = [1, 3, 6, 24, 55, 78, 454, 555, 1234, 6900]
ret1 = bisect.bisect(list1, x1)  #获取插入位置
ret2 = bisect.insort(list2, x2)  #返回插入结果

print("返回值：", ret1)
print("list1 = ", list1)
print("返回值：", ret2)
print("list1 = ", list2)