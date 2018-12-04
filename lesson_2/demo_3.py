"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/19 8:58
@welcome To Learn AI
@dist:用字典，集合做计算
"""

from __future__ import print_function

p1 = [10,20]
p2 = [14,34]

dist = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
print(dist)

p1 = {'x':10,'y':20}
p2 = {'y':34,'x':14}
dist = ((p1['x']-p2['x'])**2 + (p1['y']-p2['y'])**2)**0.5
print(dist)