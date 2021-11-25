# -*-coding:utf-8\-*-

import hashlib

def md5sum(file_name):
    with open(file_name,'rb') as f:
        hash_file = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            hash_file.update(chunk)
            chunk = f.read(8192)
