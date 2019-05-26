# -*- coding: utf-8 -*-
# author:xls
"""
    shutil模块实现文件内容拷贝、递归复制目录、解压缩文件
"""
import shutil

with open(r'd:\1.txt') as s, open(r'd:\2.txt','w') as d:
    shutil.copyfileobj(s,d)
shutil.copyfile(r'd:\1.txt',r'd:\3.txt')

from shutil import copytree, ignore_patterns
copytree('folder1', 'folder2', ignore=ignore_patterns('*.pyc', 'tmp*'))
copytree('f1', 'f2', symlinks=True, ignore=ignore_patterns('*.pyc', 'tmp*'))  #symlinks 忽略软链接

shutil.make_archive(r'd:\3',format='zip',base_dir=r'd:\a') #压缩文件夹
shutil.unpack_archive(r'd:\3.zip',r'd:\333',format='zip')  #解压文件