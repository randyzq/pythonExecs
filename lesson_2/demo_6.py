"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/30 11:02
@welcome To Learn AI
"""

def eudistance(p1,p2):
    dist = 0
    if len(p1) != len(p2):
        print('can not compute distance!')
        return -1

    for i1,i2 in zip(p1,p2):
        if i1<0 or i2<0:
            dist = -1
            break
        dist += (i1-i2)**2
    else:
        #print('in else')
        dist = dist ** 0.5
    return dist

if __name__=='__main__':
    print(eudistance((10,20),(21,55)))