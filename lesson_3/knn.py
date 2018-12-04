#!/user/bin/python
# encoding:utf-8
from __future__ import print_function

"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/12/4 17:08
@welcome To Learn AI
"""

from lesson_3.point import Point
class KNN(object):
    def __init__(self, k=5):
        pass

    def _k_nearest_neighbors(self, x, k):
        distances = []
        p = Point(x)
        for id, x2 in enumerate(self.X):
            p2 = Point(x2)
            dist = p.dist(p2)
            distances.append((dist, self.y[id]))
        distances.sort(key=lambda x: x[0])
        return distances[:k]

    def fit(self, X, y=None):
        self.X = X
        self.y = y

    # def predict(self, x, k=5):
    #     ky = self._k_nearest_neibours(x,k)
    #     return ky

    def predict(self, x, k=5):
        ky = self._k_nearest_neighbors(x, k)
        # return ky
        k_dict = {}
        for dist, type in ky:
            if type in k_dict.keys():
                k_dict[type] += 1
            else:
                k_dict[type] = 1

        k_s = sorted(k_dict, key=lambda x: x[1])
        # return k_s[0]
        return ky