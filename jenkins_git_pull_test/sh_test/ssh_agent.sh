#!/bin/bash

eval $(/usr/bin/ssh-agent -s)
ssh_passphrase=linux,123
ssh_key_path=/mnt/e/github/gitee_key/gitlab_test
ssh_passphrase_path=/mnt/e/github/sh_test/ssh_pass
echo ${ssh_passphrase}
echo "echo ${ssh_passphrase}" > ${ssh_passphrase_path}
chmod +x ${ssh_passphrase_path}
echo ${ssh_key_path}


DISPLAY=1 SSH_ASKPASS="${ssh_passphrase_path}" ssh-add ${ssh_key_path} < /dev/null
ssh-add -l
#$(/usr/bin/ssh-agent -s)


