# -*- coding: utf-8 -*-
# author:xls
"""
    re模块 正则表达式匹配
"""
import re
str = '<table><tr><td>苹果</td><td>桃子</td><td>香蕉</td></tr></table>'
reg =  re.compile(r'<td>(.*?)</td>')
result = re.findall(reg, str)
print(result)
s = """
<p>水调歌头·明月几时有\n
宋代：苏轼\n
\n
丙辰中秋，欢饮达旦，大醉，作此篇，兼怀子由。\n
\n
明月几时有？把酒问青天。\n
不知天上宫阙，今夕是何年。\n
我欲乘风归去，又恐琼楼玉宇，高处不胜寒。\n
起舞弄清影，何似在人间？\n
转朱阁，低绮户，照无眠。\n
不应有恨，何事长向别时圆？\n
人有悲欢离合，月有阴晴圆缺，此事古难全。\n
但愿人长久，千里共婵娟。\n</p>
"""

ret = re.search(r'<p>(.+)</p>', s ,re.S)
print(ret)
print(ret.group(1))