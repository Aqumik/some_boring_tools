# -*- coding:UTF-8 -*-

import subprocess


#run方法

#执行ls -l /dev/null
subprocess.run(["ls","-l","/dev/null"])

#Popen() 方法 ,子进程的创建和管理都需要使用
#创建一个子进程，执行简单的命令
p = subprocess.Popen('ls -l',shell=True)
p.returncode
p.wait()
#进程终止会返回returncode，输出值为0，否则会返回None
print(p.returncode)


def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(2)
    if subp.poll() == 0:
        #communicate 和子进程交换，发送和读取数据
        print(subp.communicate()[0])
    else:
        print('失败')

cmd('java -version')
cmd('python --version')

