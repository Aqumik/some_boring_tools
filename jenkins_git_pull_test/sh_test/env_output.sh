#!/bin/bash

eval $(/usr/bin/ssh-agent -s)
ssh_passphrase=linux,123
ssh_key_path=/e/github/gitee_key/gitlab_test
ssh_passphrase_path=/e/github/sh_test/ssh_pass
echo ${ssh_passphrase}
echo "echo ${ssh_passphrase}" > ${ssh_passphrase_path}
chmod +x ${ssh_passphrase_path}
echo ${ssh_key_path}

# https://unix.stackexchange.com/questions/571741/how-to-pass-a-passphrase-to-ssh-add-without-triggering-a-prompt
# 直接把密码传到密钥，不需要使用except模块进行自动交互
DISPLAY=1 SSH_ASKPASS="${ssh_passphrase_path}" ssh-add ${ssh_key_path} < /dev/null
ssh-add -l

env_var=(SSH_AGENT_PID SSH_AUTH_SOCK)
declare -A output_dict

for i in ${env_var[*]};
do
    output_dict[${i}]=`env|grep ${i}|awk -F '=' '{print $2}'`
done




output_fun(){
	printf "{\n"
	printf '\t"data":[\n'
	#for ((i=0;i<${#output_dict[@]};i++))
	for ie in ${!output_dict[*]};
	do
	        printf '\t\t{\n'
	        printf "\t\t\t\"${ie}\":\"${output_dict[${ie}]}\"}\n"
	done
	printf "\t]\n"
	printf "}\n"	

}

test1(){
	echo "this is 1"
}

output_fun  > /e/github/sh_test/1231234_output
