# encoding: utf-8

"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/30 15:25
@welcome To Learn AI
@desc 类的初始化
"""

class Point(object):
    #构造函数
    def __init__(self,*c):
        self.c = c

    def dist(self,p2):
        dist = 0
        if len(self.c) != len(p2.c):
            print('can not compute distance!')
            return -1

        for i1, i2 in zip(self.c, p2.c):
            if i1 < 0 or i2 < 0:
                dist = -1
                break
            dist += (i1 - i2) ** 2
        else:
            # print('in else')
            dist = dist ** 0.5
        return dist

p1 = Point(1,2,1,3,5)
p2 = Point(4,52,13,31,2)

if __name__=='__main__':
    print(p1.dist(p2))
    print(p2.dist(p1))
