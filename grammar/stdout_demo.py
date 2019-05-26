# -*- coding: utf-8 -*-
# author:xls
"""
    生成一个100%进度条
"""
import sys
import time

def bar(num,total):
    rate = num/total
    rate_num = int(rate*100)
    if num%2:
        s = '\r[%s%s]%s%%'%("="*int(num/2)," "*int((100-num)/2+1),rate_num)
    else:
        s = '\r[%s%s]%s%%'%("="*int(num/2)," "*int((100-num)/2),rate_num)
    sys.stdout.write(s)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(101):
        time.sleep(0.1)
        bar(i, 100)
