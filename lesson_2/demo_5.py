from __future__ import  print_function

"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/25 23:28
@welcome To Learn AI
"""
import time


t1 = time.time()
x = range(1,100000000)
t2 = time.time()
y = xrange(1,100000000)
t3 = time.time()

print(t2-t1,t3-t2)