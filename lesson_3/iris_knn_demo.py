#!/user/bin/python
# encoding:utf-8
from __future__ import print_function

"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/12/4 17:53
@welcome To Learn AI
"""
from knn import KNN
def prepare_data():
    X = []
    y = []

    # f = open('iris.csv')
    # for line in f:
    #     line
    #
    # f.close()

    with open('iris.csv') as f :
        for id,line in enumerate(f) :
            if id == 0 :
                continue
            segs = line.strip().split(',')
            #头4个
            X.append([float(i) for i in segs[:4]])
            #最后一个
            y.append(segs[-1])
    return X,y


if __name__=='__main__':
    X, y = prepare_data()
    model = KNN()
    model.fit(X, y)

    sample = [4.6,3.4,1.4,0.3]
    #print(model.predict(sample, k=9))

    list = [[]] * 5

    list[0].append(10)

    print(list)



