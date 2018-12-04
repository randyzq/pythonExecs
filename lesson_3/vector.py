"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/30 18:19
@welcome To Learn AI
"""
from point import Point

class Vector(Point):
    def norm(self):
        # oc = []
        # for i in self.cor:
        #     oc.append(0)
        # o = Point(oc)
        o = Point([0 for i in self.cor])
        return self.dist(o)

    def dot(self, v2):
        result = 0
        for i, j in zip(self.cor, v2.cor):
            result += i*j
        return result

    def cosin(self, v2):
        o = Point([0 for i in self.cor])
        #o = Point([0] * len(self.c))
        d1 = self.dist(o)
        d2 = v2.dist(o)
        result = 1.0 * self.dot(v2) / (d1*d2)
        return result