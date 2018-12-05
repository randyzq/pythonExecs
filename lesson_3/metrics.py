#!/user/bin/python
# encoding:utf-8
from __future__ import print_function

"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/12/5 10:49
@welcome To Learn AI
"""

class Metrics(object):
    @classmethod
    def precision(cls, y, y_pred):
        cnt = 0
        for y1, y2 in zip(y, y_pred):
            if y1 == y2:
                cnt += 1.0
            return cnt / len(y)

if __name__ == '__main__':
    y = [1, 2, 3]
    y_pred = [1, 2, 4]
    print(Metrics.precision(y, y_pred))

