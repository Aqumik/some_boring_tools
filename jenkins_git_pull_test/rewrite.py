# -*- coding:UTF-8 -*-
import os

file_path1='/Users/aqumik/Desktop/git_test/push_test'
print('当前工作目录为%s'%(os.getcwd()))
print('修改工作目录')
os.chdir(file_path1)
print('当前工作目录为%s'%(os.getcwd()))


with open('test1','w') as i:
    i.write('halo gitlab3\n')