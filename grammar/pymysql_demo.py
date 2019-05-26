# -*- coding: utf-8 -*-
# author:xls
"""
    pymysql模块,操作mysql
"""

import pymysql
conn = pymysql.connect(host='192.168.0.105',port=3306,user='xielinshai',password='3253832',db='djangotest')

cursor = conn.cursor()
sqlstr1 = "insert into student values (2,'lxt','female', '27');"
sqlstr2 = "select * from student;"
effect_row = cursor.execute(sqlstr2)
info_all = cursor.fetchall()
print(info_all)
conn.commit()
cursor.close()
conn.close()
