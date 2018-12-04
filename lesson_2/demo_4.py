"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/23 9:41
@welcome To Learn AI
@desc: 计算高位两点距离
"""

from __future__ import print_function

p1 = [11,25,35,54,64,58,54,22,11]

p2 = [21,34,22,73,65,44,83,73,16]

dist = 0

if len(p1) != len(p2) :
    print('can not compute distance.')
    exit(1)

for i1,i2 in zip(p1,p2):
    dist +=(i1-i2)**2

dist = dist**0.5

print(dist)




