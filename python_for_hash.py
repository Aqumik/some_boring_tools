# -*-coding:utf-8-*-

import hashlib

# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
# https://sjq597.github.io/2015/12/18/Python-MD5%E6%A3%80%E9%AA%8C%E6%96%87%E4%BB%B6/
def md5sum(file_name):
    with open(file_name,'rb') as f:
        hash_file = hashlib.md5()
        chunk = f.read(8192)
        while chunk:
            hash_file.update(chunk)
            chunk = f.read(8192)
    return hash_file.hexdigest()

f1 = '/Users/aqumik/Desktop/git_test/TD/gitlab/cubickill-prod/cubickill-sql/pjtd-sql.zip'
a = md5sum(f1)
print(a)