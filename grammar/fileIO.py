# -*- coding: utf-8 -*-
# author:xls
"""
    使用with上下文管理器读写文件
"""
with open(r'd:\\test1.txt') as f1 ,open(r'd:\\test2.txt','w') as f2:
    line = f1.read()
    f2.write(line)
