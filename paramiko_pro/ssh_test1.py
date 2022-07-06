# -*- coding:UTF-8 -*-
'''
@Date    ：2022/2/22 5:52 下午 
@Author  ：aqumik
NO ERROR !!!
NO ERROR !!!
NO ERROR !!!
'''
import paramiko


# ssh = paramiko.SSHClient()


def ssh(ip, port, username, password, cmd):
    try:
        ssh = paramiko.SSHClient()  # 创建ssh对象
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=int(port), username=username, password=password, )
        stdin, stdout, stderr = ssh.exec_command(cmd, timeout=10)
        result = stdout.read()
        result1 = result.decode()
        print(result1)
        error = stderr.read().decode('utf-8')
        print(error)

        if not error:
            ret = {"ip": ip, "data": result1}
            ssh.close()
            return ret
    except Exception as e:
        error = "账号或密码错误,{}".format(e)
        ret = {"ip": ip, "data": error}
        return ret


if __name__ == '__main__':
    ssh('10.10.16.80',22,'root','linuxlskadjlfkajdlfj','python3 /opt/TD_test/gitlab/thread_unzip_v2.py -b "c-en-prod" -p "\\10.10.10.118\publish\pjtd\c-stage\\20220221144800"')
