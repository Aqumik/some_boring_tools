# -*- coding:UTF-8 -*-

import platform
import os
from git import Repo, Actor
import git
"""
    1、如何提交git内容？
"""

class Git_push_test(object):
    def __init__(self,authorer,repo_url):
        self.authorer = authorer
        self.repo_url = repo_url
        self.repo = None


    def push_autor(self,authorer):
        author_email = authorer + "qq.com"
        author_user = Actor(authorer,author_email)

    def pull(self):
        # 更新代码
        self.repo.git.pull()






