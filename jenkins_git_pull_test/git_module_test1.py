# -*- coding:UTF-8 -*-

import platform
import os
import platform
from time import sleep

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


"""
    1、当传入的环境变量不存在于远程和本地，将会创建
    2、存在于远程，不存在本地，将会重新拉取
    
"""
#分支测试
def branch_test():
    repo = git.Repo(file_path1)
    #查看当前处于本地处于的分支hash
    bra = repo.active_branch
    print(repo)
    print('当前分支',bra)


    #查看当前本地的所有分支
    all_branch = repo.branches
    print(all_branch)
    # for i in all_branch:
    #     print(i)

    repo_heads = repo.heads
    print(repo_heads)



    #切换分支
    # print('********',repo)
    # before = repo.git.branch()
    # # print('切换前的分支',before)
    # repo.git.checkout('main')
    # after = repo.git.branch()
    # print('切换分支后，当前分支的位置',after)

    #查看当前远程的所有分支
    # all_remote
    # print(repo)
    remote_refs = repo.remote().refs
    # for refs in remote_refs:
        # print(refs.name)

    remote_branches = []
    for ref in repo.git.branch('-r').split('\n'):
        print(ref)
        # .strip()  去除两端空格
        remote_branches.append(ref.strip())

    print(remote_branches)
    remote_branches_now = remote_branches[1:]
    print(remote_branches_now)
    t1 = remote_branches_now[0]
    print(t1)
    print(type(t1))
    sha2 = repo.rev_parse(t1)
    # repo.rev_parse()
    print(sha2)

    # for remote in repo.remotes:
        # print('------',remote)
        # remote.fetch()

    o = repo.remotes.origin
    print(repo.rev_parse('origin/main'))
    print('---------正在刷新')
    o.fetch('main')

    # r1.fetch()
    print(repo.rev_parse('main'))
    print(repo.rev_parse('origin/main'))
    print('--------',o)



    # print(t1)
    # print(repo.rev_parse('origin/main')
    #使用使用git命令去获取所有分支
    # repo2 = git.Git(file_path1)
    # print(repo2.branch())



# branch_test()


def hash_check():
    local_branch = 'main'
    repo = git.Repo(file_path1)
    repo_name = 'origin'
    remote_branch = repo_name + '/' +local_branch
    # print(remote_branch)
    local_commit_hash = repo.rev_parse(local_branch)
    remote_commit_hash = repo.rev_parse(remote_branch)




    #更新指定的远程分支库

    print('-----------更新前远程库hash')
    print(repo.rev_parse(local_branch))
    print(remote_commit_hash)
    remote_fetch = repo.remotes.origin
    remote_fetch.fetch('main')

    print('-----------更新后远程库hash')
    print(repo.rev_parse(local_branch))
    print(repo.rev_parse(remote_branch))

    bra = repo.active_branch
    print('当前分支',bra)


    # remote_fetch.pull()



    print(repo.rev_parse('origin/main'))
    if local_commit_hash == remote_commit_hash:
        print('本地仓库与远程仓库Hash一致')
        print('当前分支为：%s\n本地仓库Hash为：%s\n远程仓库Hash为：%s'%(local_branch,local_commit_hash,remote_commit_hash))
    else:
        print("本地仓库与远程仓库Hash不一致")
        # sleep(10)
        # print('dlsfjaljf')

hash_check()




#对比md5模块
def md5_check():
    repo = git.Repo(file_path1)
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
    # sha3 = git.cmd.Git().ls_remote(repo_url)
    # print(sha3)

    #git fetch更新远程仓库
    #如何指定远程分支更新？
    # print(repo)
    print(repo.remotes)

    # for remote in repo.remotes:
    #     print('------',remote)
    #     remote.fetch()

    #查看当前所有远程分支,


    #查看当前本地所有分支


#
# md5_check()




# git_url='git@gitlab.cokutau.cn:duweizhi/push_test.git'
# # repo = Repo(file_path1)
# new_repo = git.Repo.clone_from(url='git@gitlab.cokutau.cn:duweizhi/push_test.git',to_path='newww')

# repo2 = git.Git(file_path1)
# print(repo2.status())




