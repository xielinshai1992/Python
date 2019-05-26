# -*- coding: utf-8 -*-
# author:xls
"""
    使用hashlib模块提供的摘要算法 如md5、sha1、sha256、sha512、shake_256...
"""
import hashlib
h = hashlib.sha256()   #获得一个hash对象
print(h.digest_size, h.name)  # 打印hash结果的长度、hash算法名称
h.update(b'i love python')  #使用hash对象的update方法添加消息
s = h.hexdigest()     # 获得16进制str类型的消息摘要
print(s)
