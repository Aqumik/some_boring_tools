# -*- coding:UTF-8 -*-

import os
import sys

push_root_dir = '/Users/aqumik/Desktop/git_test/11'

file_name = 't4'
push_usr_dir = push_root_dir + '/' + file_name
# print(push_root_dir)
a = 2
#切换到存放推送文件的根目录
os.chdir(push_root_dir)
# print(os.getcwd())
def file_exists():
    # print()
    # result = os.path.exists('t1')
    if not os.path.exists(file_name):
        print('推送目录不存在，将会从仓库拉取....')
        return 3
        # os.makedirs('tt1')
    else:
        try:
            os.chdir(push_usr_dir)
        except Exception:
            print("文件名：%s 的文件类型有问题，请检查...(如：目录下有同名的文件，而不是文件夹)"%(file_name))
            print("程序已中止.....")
            sys.exit(1)
        print('切换目录到对应项目下： %s'%(push_usr_dir))
        #判断基准为是否有 ".git"目录
        if not os.path.exists('.git'):
            print("此文件不存在")
            return 1
        else:
            print("此文件存在")
            return 2
# print(file_exists())


#接收 file_exits函数返回值再做适当的初始化
def git_init_action(file_return):
    if file_return == 3:
        print('推送目录不存在，将会从远程仓库进行拉取....')
    elif file_return == 2:
        print("项目本地Git仓库已存在")
    elif file_return == 1:
        print("项目文件夹存在，但并没有检查到本地Git仓库")
        print("将会重新拉取...")
    else:
        print('程序中止，返回值有问题')
        sys.exit(1)



git_init_action(file_exists())