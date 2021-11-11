# -*- coding:UTF-8 -*-

import os
import sys

import git
from git import Repo,RemoteProgress

from tqdm import tqdm
#删除非空目录
import  shutil


push_root_dir = '/Users/aqumik/Desktop/git_test/11'
#file_name 必须是项目的文件夹
file_name = 't4'
push_usr_dir = push_root_dir + '/' + file_name
branch_name = 'master'
repo_url = 'git@gitee.com:chetimberk/test.git'
SSH_AUTH_SOCK = '/var/folders/f9/vgqgcqy92vb6d_njsxgm5sz80000gn/T//ssh-FXMs7YvI8Kvy/agent.48496'
commit_content = 'Halo guys!'
os.environ['SSH_AUTH_SOCK'] = SSH_AUTH_SOCK

jenkins_output_path = '/Users/aqumik/Desktop/git_test/jenkins_output/project1'
#切换到存放推送文件的根目录
os.chdir(push_root_dir)



# file_path1 = '/Users/aqumik/Desktop/git_test/11/test1'

# 代码克隆进度条功能
# https://stackoverflow.com/questions/51045540/python-progress-bar-for-git-clone/62623518#62623518
class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()






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
            print("项目文件夹存在，但并没有检查到本地Git仓库")
            return 1
        else:
            print("此文件存在")
            return 2
# print(file_exists())


#接收 file_exits函数返回值再做适当的初始化
def git_init_action(file_return):
    print(os.getcwd())
    if file_return == 3:
        print('推送目录不存在，将会从远程仓库进行拉取....')
        Repo.clone_from(repo_url, push_usr_dir, branch=branch_name, progress=CloneProgress())

    elif file_return == 2:
        print("项目本地Git仓库已存在")
    elif file_return == 1:
        print("项目文件夹存在，但并没有检查到本地Git仓库")
        print("将会删除项目文件夹，并重新拉取...")
        #此处的处理方法两种： 1、原脚本是直接初始化仓库，新建分支与当前分支建立映射；2、清空重拉。因为此处只做中转作用，没必要大费周章去处理
        #当前处理方法..
        #1、退出当前项目文件；2、删除项目文件；3、重新git clone
        #切换回推送根目录
        os.chdir(push_root_dir)
        # os.removedirs(push_usr_dir)
        #删除非空目录
        shutil.rmtree(push_usr_dir)
        Repo.clone_from(repo_url, push_usr_dir, branch=branch_name, progress=CloneProgress())
    else:
        print('程序中止，git_init_action模块接收的返回值异常')
        sys.exit(1)

#jenkins编译出来的文件处理模块
#处理的内容：1、清空当前目录下所有文件    2、将 jenkins编译出的文件复制到 当前项目文件夹下

    
#jenkins获取到的workspace工作目录 /var/lib/jenkins/workspace/master-build   master-build为项目的名字
def file_handle_module():





# def git_push_action()



git_init_action(file_exists())