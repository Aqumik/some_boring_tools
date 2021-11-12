# -*- coding:UTF-8 -*-

import os
import sys
import git
from git import Repo,RemoteProgress
from tqdm import tqdm
#删除非空目录
import  shutil


class Git_module(object):
    def __init__(self,push_root_dir,file_name,jenkins_output_path,repo_url,local_branch_name,commit_content,repo_name,remote_branch_name):
        #本地系统环境部分
        self.push_root_dir = push_root_dir
        self.file_name = file_name
        self.push_usr_dir = os.path.join(push_root_dir,file_name)
        self.jenkins_output_path = jenkins_output_path

        #本地Git仓库部分
        self.repo_url = repo_url
        # self.branch_name = branch_name
        self.local_branch_name = local_branch_name
        self.commit_content = commit_content
        self.repo_name = repo_name

        #远程仓库部分
        self.remote_branch_name = remote_branch_name

        #实例化对象
        self.repo = git.Repo(self.push_usr_dir)


    #Hash模块
    def hash(self):
        # print(self.repo_name)



if __name__ == '__main__':
    push_root_dir = '/Users/aqumik/Desktop/git_test/11'
    file_name = 't4'
    jenkins_output_path = '/Users/aqumik/Desktop/git_test/jenkins_output/project1'
    repo_url = 'git@gitee.com:chetimberk/jenkins-test1.git'
    local_branch_name = 'master'
    commit_content = 'hahahahahahahahah'
    repo_name = 'origin'
    remote_branch_name = 'master'
    g = Git_module(push_root_dir,file_name,jenkins_output_path,repo_url,local_branch_name,commit_content,repo_name,remote_branch_name)
    g.hash()