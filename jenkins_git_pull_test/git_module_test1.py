# -*- coding:utf-8 -*-

import platform


#判断系统类型，后续用于执行哪些步骤，主要为windows和linux
def system_type():
    if platform.system().lower() == 'windows':
        print('windows')
    elif platform.system().lower() == 'linux':
        print('linux')
    else:
        print('Other System')


system_type()
