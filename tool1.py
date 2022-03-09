# -*- coding:utf-8 -*-
#1、读取文本信息
#2、轮询输出

import os


#可以批量生成删除数据库命令
#用法，在数据库得到的表直接复制，去掉 '|'，即可
def hhhh():
    path = os.getcwd()
    print(path)
    file = open('1.txt')
    for each_line in file:
        resutl = format(str(each_line))
        #去除换行
        resutl = resutl.strip('\n')
        resutl2 = resutl
        # print('%s'%resutl)
        print('drop database%s ;'%(resutl))
        # print('mysqldump -uroot -pjsjs123456# -h diyibo-mysql-server1 --databases %s > /tmp/sql/%s.sql '%(resutl,resutl2))



def test2():
#读取1.txt文件内容，把所有关键内容输出到指定命令中，实现效果: I am test1 test2 test3 test4
    path = os.getcwd()
    print(path)
    file = open('1.txt')
    re = ''

    for each_line in range(1,20):
        # 去除换行
        resutl1 = format(str(each_line)) + ','
        re += resutl1
        print(re)
    print('rm -rf %s/ '%(re))
    # print(li)
    re2 = ''
    for each_line2 in range(1,31):
        if each_line2 < 10:
            resutl2 = str('2021060') + format(str(each_line2)) + '/ '
            resutl2 = format(str(resutl2))
        else:
            resutl2 = str('202106') + format(str(each_line2)) + '/ '
        re2 +=  resutl2
    print('rm -rf %s '%(re2))




def excel_date():
    # print('2021-6-3.py  18:00:00')
    for i in range(1,32):
        print('2021-10-%i  10:00:00'%(i))
        print('2021-10-%i  18:00:00' % (i))



# 输出1到100

def echo_100():
    list1 = []
    list2 = []
    list3 = list(range(601,901))
    for i in list3:
        list1.append(i)
    for x in list1:
        print(x,end=",")

#输出奇偶出
def echo_jiou():
    list1 = []
    list2 = []
    list3 = list(range(1601,2001))
    for i in list3:
        if (i % 2) == 0:
            list1.append(i)
        else:
            list2.append(i)
    for x in list1:
        print(x,end=',')
    print('\n')
    for x in list2:
        print(x,end=',')


if __name__ == "__main__":

    print('-----------')
    echo_100()
