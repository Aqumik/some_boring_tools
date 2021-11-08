# -*- coding:utf-8 -*-



import git
import os
from getpass import getpass
#使用gitee
from git import Git, Repo

file_path1='/Users/aqumik/Desktop/git_test/11/'
new1=''
repo_url='git@gitee.com:chetimberk/test.git'
# repo_url='git@github.com:Aqumik/go_learnning.git'
git_ssh_identify_file='/Users/aqumik/Documents/ssh_key/no_pass_gitlab'
os.chdir(file_path1)


# from jenkins_git_pull_test.askpass import username
username = 'chetimberk'
getpass = 'linux,123'
project_dir = os.path.dirname(file_path1)
print(project_dir)
SSH_AUTH_SOCK='/var/folders/f9/vgqgcqy92vb6d_njsxgm5sz80000gn/T//ssh-lekiOvj3pCcU/agent.41839'
print(os.environ.keys())
# os.environ['GIT_ASKPASS'] = os.path.join(project_dir, 'askpass.py')
os.environ['SSH_AUTH_SOCK'] = SSH_AUTH_SOCK
# os.environ['GIT_PASSWORD'] = getpass


# git_ssh_identify_file = os.path.expanduser('~/Documents/ssh_key/no_pass_gitlab')
# git_ssh_cmd = 'ssh -i /Users/aqumik/Documents/ssh_key/no_pass_gitlab'
# print(git_ssh_cmd)
# with Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
Repo.clone_from(repo_url, file_path1, branch='master')

# os.close()
# g = git.cmd.Git('/path/to/some/local/repo')
# g.pull()