# -*- coding:UTF-8 -*-

import platform
import os
from git import Repo,Actor
import git
"""
    1、如何提交git内容？
"""

# file_path='/Users/aqumik/Desktop/git_test/push_test'
file_path1='/Users/aqumik/Desktop/git_test/push_test'
new1=''
repo_url='git@git.cokutau.cn:duweizhi/push_test.git'
#判断系统类型，后续用于执行哪些步骤，主要为windows和linux
def system_type():
    if platform.system().lower() == 'windows':
        print('windows')
    elif platform.system().lower() == 'linux':
        print('linux')
    else:
        print('Other System')

print('当前工作目录为%s'%(os.getcwd()))
print('修改工作目录')
os.chdir(file_path1)
print('当前工作目录为%s'%(os.getcwd()))




def push_autor():
    autorer = Actor("dflkjdsf","flajflajlfkja@co.com")
    commiter = Actor("bigbigbro","bigbigbro@qq.com")

    # print(push_autor())
    repo = Repo(file_path1)
    index = repo.index
    # repo.git.pull()

    # print(index.diff())
    index.add(['*'])
    index.commit('this is python test2',author=autorer,committer=commiter)
    repo.git.push()

# push_autor()



#对比md5模块
def md5_check():
    repo = git.Repo(file_path1)
    # sha = repo.head.object.hexsha
    sha1 = repo.rev_parse('main')
    # 如何查看当前的HEAD？
    #查看当前处于本地处于的分支hash
    bra = repo.active_branch

    print(repo)
    print('当前分支',bra)
    print(sha1)
    print('----------')
    #如何更新远程分支？
    # remote = repo.create_remote(name='origin',url=git_url)
    sha2 = repo.rev_parse('origin/main')
    remote = repo.remote()
    print(sha2)
    remote = remote.repo.head.object.hexsha
    # remote = remote.head.object.hexsha
    # print(remote)
    # empty_repo = git.Repo.init(os.path.join(file_path1,'empty'))
    # origin = empty_repo.create_remote('origin',repo.remote.origin.url)
    # assert
    # sha2 = repo.remotes.head.object.hexsha
    # print(origin)
    # print(sha2)
    sha3 = git.cmd.Git().ls_remote(repo_url)
    print(sha3)



md5_check()

# git_url='git@gitlab.cokutau.cn:duweizhi/push_test.git'
# # repo = Repo(file_path1)
# new_repo = git.Repo.clone_from(url='git@gitlab.cokutau.cn:duweizhi/push_test.git',to_path='newww')

# repo2 = git.Git(file_path1)
# print(repo2.status())




