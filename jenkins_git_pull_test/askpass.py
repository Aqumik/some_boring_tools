# -*- coding:utf-8 -*-

from sys import argv
from os import environ


# username = 'test'
if 'username' in argv[1].lower():
    print(environ['GIT_USERNAME'])
    exit()

if 'password' in argv[1].lower():
    print(environ['GIT_PASSWORD'])
    exit()

exit(1)