# -*- coding:UTF-8 -*-
'''
@Date    ：2022/2/14 10:42 上午 
@Author  ：aqumik
NO ERROR !!!
NO ERROR !!!
NO ERROR !!!
'''

# 学习如何使用Redis
import redis
import random_string
db_num = 5
r = redis.StrictRedis(host='10.10.16.80', port=6667, db=db_num,password='linux3')
loop_num = db_num * 100 + 1
for i in range(1,loop_num):
    # print(i)
    key_num = 'd1' + str(i)
    # print(key_num)
    value = str(random_string.random_func().per_info())
# print(type(value))
# print(value)
# print(value)
    r.set(key_num,value)

