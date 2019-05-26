# -*- coding: utf-8 -*-
# author:xls
"""
    zipfile模块，读写.zip文件，实现解压缩
"""

import zipfile

with zipfile.ZipFile(r'd:\test.zip','w') as z:
    z.write(r'd:\1.txt')
    z.write(r'd:\学习任务.txt')
    z.close()
with zipfile.ZipFile(r'd:\test.zip') as z:
    z.extractall('D:\\')