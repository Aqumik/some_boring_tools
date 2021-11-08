# -*- coding:UTF-8 -*-
import base64
import platform
import os
import platform
import tempfile
from time import sleep

from git import Repo,Actor,Git
from subprocess import Popen, PIPE
import git


#使用gitee
file_path1='/Users/aqumik/Desktop/git_test/11'
new1=''
repo_url='git@gitee.com:chetimberk/test.git'
# repo = git.Repo(file_path1)

print('当前工作目录为%s'%(os.getcwd()))
print('修改工作目录')
os.chdir(file_path1)
print('当前工作目录为%s'%(os.getcwd()))


# 密钥模块
# 如何输入密码？
# 推送初始化模块
# Git 2.3以上可用
def ssh_key_module():
    # os.path.expanduser()转化为User目录
    git_ssh_identify_file = os.path.expanduser('~/Documents/ssh_key/gitlab_test')
    git_ssh_cmd = 'ssh -i %s' % git_ssh_identify_file
    with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
        Repo.clone_from(repo_url, file_path1, branch='master')
    # print(ssh_cmd)
    # with repo.git.custom_environment(GIT_SSH_COMMAND=ssh_cmd):
    #     repo.remotes.origin.fetch()


# ssh_key_module()

def test1():
    process = Popen(["git", "clone",repo_url], stdin=PIPE)
    b1 = str.encode("linux,123")
    process.communicate(b1)
# test1()


def test2():
    private_key_pat = os.path.expanduser('~/Documents/ssh_key/gitlab_test')
    _git_private_key = base64.b64decode('linux,123')
    print(_git_private_key)
    _git_private_file = tempfile.NamedTemporaryFile()
    print(_git_private_file.name)
    _git_private_file.write(_git_private_key)
    _git_private_file.flush()
    t1 = _git_private_file.read()
    print(t1)
    # sleep(30)

    git_ssh_cmd = 'ssh -i %s' % private_key_pat
    with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
        Repo.clone_from(repo_url, file_path1, branch='master')

    _git_private_file.close()
test2()

