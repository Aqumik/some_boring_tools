# -*- coding:UTF-8 -*-
import json
import platform
import os
import platform
import subprocess
from time import sleep

from git import Repo,Actor
import git


file_path1='/Users/aqumik/Desktop/git_test/push_test'
new1=''
repo_url='git@git.cokutau.cn:duweizhi/push_test.git'



print('当前工作目录为%s'%(os.getcwd()))
print('修改工作目录')
os.chdir(file_path1)
print('当前工作目录为%s'%(os.getcwd()))
repo = git.Repo(file_path1)

#Hash检验模块，用于校验远程仓库本地的情况
def hash_check():
    #第一次Hash，即hash_1，在未拉取前；第二次Hash，即hash_2，拉取后
    local_branch = 't1'
    repo = git.Repo(file_path1)
    repo_name = 'origin'
    remote_branch = repo_name + '/' +local_branch
    repo.git.checkout(local_branch)
    print('切换分支到%s'%local_branch)

    # print(remote_branch)

    local_commit_hash = repo.rev_parse(local_branch)
    remote_commit_hash_1 = repo.rev_parse(remote_branch)

    #更新指定的远程分支库
    print('-----------更新前远程的%s库hash'%local_branch)
    print(repo.rev_parse(local_branch))
    print(remote_commit_hash_1)
    remote_fetch = repo.remotes.origin
    # remote_fetch.fetch('main')
    #切换分支到main，尝试fetch是针对单个分支还是全部分支？ --若使用fetch()会把全部远程分支更新，所以需要指定特定分支
    remote_fetch.fetch(local_branch)

    # local_commit_hash = repo.rev_parse(local_branch)
    remote_commit_hash_2 = repo.rev_parse(remote_branch)

    print('-----------更新后远程的%s库hash'%local_branch)
    print(repo.rev_parse(local_branch))
    print(remote_commit_hash_2)


    print('************%s'%repo.rev_parse('origin/main'))

    bra = repo.active_branch
    print('当前分支',bra)
    if local_commit_hash == remote_commit_hash_2:
        print('本地仓库与远程仓库Hash一致')
        print('当前分支为：%s\n本地仓库Hash为：%s\n远程仓库Hash为：%s'%(local_branch,local_commit_hash,remote_commit_hash_2))
    else:
        print("本地仓库与远程仓库Hash不一致，将会自动进行更新......")
        print("本地仓库Hash为%s\n远程仓库Hash为%s"%(local_commit_hash,remote_commit_hash_2))
        # sleep(4)
        #要指定拉取的分支，否则会拉取全部分支到本地
        remote_fetch.pull(local_branch)
        print('************%s' % repo.rev_parse('origin/main'))
        print('更新完成，当前本地Hash为%s\n'%(repo.rev_parse(local_branch)))
        # print('dlsfjaljf')



    list1 = ['main','origin/main','t1','origin/t1']
    for i in list1:
        print('当前分支为%s,commit的Hash为%s'%(i,repo.rev_parse(i)))
        # print(i)


# Windows   提取ssh-agent环境参数模块
# 后续需要杀死进程
def win_get_ssh_env():
    git_bash_run_ssh_agent = subprocess.Popen(
        ["C:\Program Files\Git\git-bash.exe",
         "E:\github\some_boring_tools\jenkins_git_pull_test\sh_test\env_output.sh"],
        bufsize=1,
        stdin=None,
        stdout=None,
        stderr=None,
        preexec_fn=None,
        close_fds=True,
        shell=False,
        #cwd变量是否可以不要？
        cwd="E:\github\some_boring_tools\jenkins_git_pull_test",
    )
    git_ssh_identify_file = '/Users/aqumik/Documents/ssh_key/no_pass_gitlab'
    ssh_auth_json_file = '/Users/aqumik/Desktop/Github/some_boring_tools/jenkins_git_pull_test/sh_test/git_bash_output.json'
    read_json = open(ssh_auth_json_file)
    data = json.load(read_json)
    # data 将会接收到类似 {'SSH_AUTH_SOCK': '/tmp/ssh-zsZD0ktYq6XD/agent.2446', 'SSH_AGENT_PID': '2447'} 的字典可以直接调用
    data = data['win_ssh_env']

    #change the os env
    #有了 SSH_AUTH_SOCK 可以直接调用该sock去提交代码，因为该sock绑定了对应的密钥
    SSH_AUTH_SOCK=data['SSH_AUTH_SOCK']
    #PID用于后续关闭对应的SSH Agent，若不关闭每次调用都会开启一个进程
    SSH_AGENT_PID=data['SSH_AGENT_PID']
    # print(os.environ.keys())
    os.environ['SSH_AUTH_SOCK'] = SSH_AUTH_SOCK
    #
    # Repo.clone_from(repo_url, file_path1, branch='master')