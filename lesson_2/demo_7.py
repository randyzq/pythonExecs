"""
author:Andy
contact:18213258@qq.com
@file:
@time: 2018/11/30 13:43
@welcome To Learn AI
@desc 流水线作业
"""

def myopen(filename):
    result=[]
    f = open(filename)
    for line in f :
        #do something
        result = line
        yield result
    f.close()

logs = myopen("test.log")
for line in logs:
    print(line)

