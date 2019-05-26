# -*- coding: utf-8 -*-
# author:xls
"""
    os.walk()内置函数，遍历文件夹下的所有子文件夹和文件
"""

import os
try:
    for root, dirs, files in os.walk(r"D:\个人记录"):
        print("\033[1;31m-"*8, "directory", "<%s>\033[0m" % root, "-"*10)
        for directory in dirs:
            print("\033[1;34m<DIR>    %s\033[0m" % directory)
        for file in files:
            print("\t\t%s" % file)
except OSError as ex:
    print(ex)
