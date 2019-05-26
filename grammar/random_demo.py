# -*- coding: utf-8 -*-
# author:xls
"""
    成一个包含大写字母A-Z和数字0-9的随机4位验证码
"""
import random
check_code = ''
for i in range(4):
    current = random.randrange(4)
    if current == i:
        #生成一个随机整数
        temp = random.randrange(10)
    else:
        #生成一个随机的大写字母
        temp = chr(random.randrange(65, 91))
    check_code += str(temp)
print(check_code)