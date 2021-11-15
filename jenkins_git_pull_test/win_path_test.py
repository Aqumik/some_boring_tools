# -*- coding:UTF-8 -*-

import os

from git import Repo

print(os.environ.keys())
push_root_dir = r'F:\test\jenkins_out'
print(os.getcwd())
print(os.chdir(push_root_dir))
print(os.getcwd())
os.environ['SSH_AUTH_SOCK'] = r"E:\tmp\user_tmp\Temp\ssh-24qXYIAg4rOw\agent.922"
repo_url = 'git@gitee.com:chetimberk/test.git'
push_usr_dir = r'F:\test\pro_root\t4'
Repo.clone_from(repo_url, push_usr_dir, branch='master')