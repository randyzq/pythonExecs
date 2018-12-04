# encoding: utf-8

"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/30 15:42
@welcome To Learn AI
@desc 继承，求夹角余弦
"""
from __future__ import print_function
from demo_9 import Point

class Vector(Point):
    def dot(self, v2):
        result = 0
        for i, j in zip(self.c, v2.c):
            result += i*j
        return result

    def cosin(self, v2):
        o = Point(*[0 for i in range(len(self.c))])
        #o = Point([0] * len(self.c))
        d1 = self.dist(o)
        d2 = v2.dist(o)
        result = 1.0 * self.dot(v2) / (d1*d2)
        return result

v1 = Vector(0, 1, 0)
v2 = Vector(3, 4, 0)

print ('dot:', v1.dot(v2))
print ('cosin:', v1.cosin(v2))
