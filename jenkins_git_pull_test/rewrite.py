# -*- coding:UTF-8 -*-
import time
import os

# file_path1='/Users/aqumik/Desktop/git_test/push_test'
# print('当前工作目录为%s'%(os.getcwd()))
# print('修改工作目录')
# os.chdir(file_path1)
# print('当前工作目录为%s'%(os.getcwd()))
#
#
# with open('test1','w') as i:
#     localtime = time.asctime( time.localtime(time.time()) )
#     i.write('%shalo gitlab3\n'%(localtime))

import sys,time
for i in range(30): #进度条类型
    sys.stdout.write("*")
    sys.stdout.flush()
    time.sleep(0.2)