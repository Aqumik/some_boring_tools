# -*- coding:UTF-8 -*-
import time
import os

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
    def __init__(self, SSH_AUTH_SOCK, SSH_AGENT_PID):
        self.SSH_AUTH_SOCK = str()
        self.SSH_AGENT_PID = int()
    def t1(self):
        a = 9
        # b = 2
        self.SSH_AUTH_SOCK = a
        self.SSH_AGENT_PID = 10
        return self.SSH_AUTH_SOCK,self.SSH_AGENT_PID
    def t2(self):
        # self.t1()
        print(self.SSH_AUTH_SOCK)
        print(self.SSH_AGENT_PID)


c = tets(1,2)
print(c.t1())
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