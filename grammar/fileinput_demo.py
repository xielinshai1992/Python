# -*- coding: utf-8 -*-
# author:xls
"""
    fileinput模块实现为文件每一行添加"#行号"
"""
import fileinput

with fileinput.input(files="d:\\test1.txt",inplace=True ) as f:
    for line in f:
        line = line.rstrip()
        num = fileinput.lineno()
        print("#%d\t%s" % (num, line))