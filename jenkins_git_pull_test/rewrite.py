# -*- coding:UTF-8 -*-
import time
import os
import git

# file_path1='/Users/aqumik/Desktop/git_test/push_test'
# print('当前工作目录为%s'%(os.getcwd()))
# print('修改工作目录')
# os.chdir(file_path1)
# print('当前工作目录为%s'%(os.getcwd()))
#
#
# with open('test1','w') as i:
#     localtime = time.asctime( time.localtime(time.time()) )
#     i.write('%shalo gitlab3\n'%(localtime))

class tets(object):
    def __init__(self,id):
        self.SSH_AUTH_SOCK = id
        self.SSH_AGENT_PID = int()
        self.repo = None
    def t1(self):
        pass
        # self.git_method()
        # print(type(self.repo))
        # return a
    def t2(self):
        # self.t1()
        numm = self.t1()
        num = numm
        if num == 1:
            print('failed')
        else:
            print('bingo')
            print(num)
        # print(self.SSH_AUTH_SOCK)
        # print(self.SSH_AGENT_PID)
    def git_method(self):
        self.repo = git.Repo('/Users/aqumik/Desktop/git_test/11/t4')
        # print(type(repo))
        print(self.repo)
        return self.repo

os.environ['SSH_AUTH_SOCK'] = '/var/folders/f9/vgqgcqy92vb6d_njsxgm5sz80000gn/T//ssh-YZcY8WFst6j7/agent.4183'

repo = git.Repo('/Users/aqumik/Desktop/git_test/11/t4')
branch_name = 'test8'
repo.create_head(branch_name)
repo.git.checkout(branch_name)
# print(repo.rev_parse(branch_name))
# remote_fetch = repo.remotes.origin
# remote_fetch.fetch(branch_name)
# c.t2()

# def foo(*args, **kwargs):
#     print('args = ', args)
#     print('kwargs = ', kwargs)
#     print('---------------------------------------')
#
# if __name__ == '__main__':
#     dic = { '1' : 1,'2' : 2 }
#     b = 1
#     c = 2
#     foo(b,c,e=2)