# -*- coding: utf-8 -*-
# author:xls
"""
    subprocess模块，创建子进程执行操作系统级别命令
"""
import subprocess
s = subprocess.run("ipconfig /all", stdout=subprocess.PIPE)
print(s.stdout.decode("GBK"))
# f = open('d:\\1.txt')
# ret = subprocess.run("python", stdin=f ,stdout=subprocess.PIPE)
# result = ret.stdout

# python控制台
s = subprocess.Popen('python',stdout=subprocess.PIPE,stdin=subprocess.PIPE,shell=True)
s.stdin.write(b'import datetime\n')
s.stdin.write(b'print(datetime.date.today())')
s.stdin.close()
out = s.stdout.read().decode('gbk')
s.stdout.close()
print(out)

