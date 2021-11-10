# -*- coding:utf-8 -*-



import git
import os
from getpass import getpass
#使用gitee
from git import Git, Repo
import json

file_path1='E:/github/test1'
new1=''
repo_url='git@gitee.com:chetimberk/test.git'
git_ssh_identify_file='/Users/aqumik/Documents/ssh_key/no_pass_gitlab'
ssh_auth_json_file='/Users/aqumik/Desktop/Github/some_boring_tools/jenkins_git_pull_test/sh_test/git_bash_output.json'

# read the json file to get the  "SSH_AUTH_SOCK" value
# open json file
f = open(ssh_auth_json_file)
# returns json object as
# type dic
data = json.load(f)
# data2 = data['win_ssh_env']
data = data['data']
# print(data2)
# print(type(data2))
SSH_AUTH_SOCK = data['SSH_AUTH_SOCK']
SSH_AGENT_PID = data['SSH_AGENT_PID']
print(SSH_AGENT_PID,SSH_AUTH_SOCK)
# project_dir = os.path.dirname(file_path1)
# print(project_dir)
# SSH_AUTH_SOCK='/tmp/ssh-Cy3ZdOv5uvXq/agent.2330'
# # SSH_AUTH_SOCK='\\var\\folders\\f9\\vgqgcqy92vb6d_njsxgm5sz80000gn\\T\\ssh-lekiOvj3pCcU\\agent.41839'
# print(os.environ.keys())
# os.environ['SSH_AUTH_SOCK'] = SSH_AUTH_SOCK
#
#
#
# print(os.environ.keys())
# Repo.clone_from(repo_url, file_path1, branch='master')


