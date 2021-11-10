#!/bin/bash

eval $(/usr/bin/ssh-agent -s)
ssh_passphrase=linux,123
#E:\github\some_boring_tools\jenkins_git_pull_test\sh_test

ssh_key_path=/e/github/gitee_key/gitlab_test
#ssh_passphrase_path=/e/github/some_boring_tools/jenkins_git_pull_test/sh_test/ssh_pass
ssh_passphrase_name=SSH_PASS
shell_output_json=git_bash_output.json
work_path=$(cd "$(dirname $0)";pwd)
cd ${work_path}



#echo ${ssh_passphrase}
echo "echo ${ssh_passphrase}" > ${ssh_passphrase_name}
chmod +x ${ssh_passphrase_name}
#echo ${ssh_key_path}

# https://unix.stackexchange.com/questions/571741/how-to-pass-a-passphrase-to-ssh-add-without-triggering-a-prompt
# 直接把密码传到密钥，不需要使用except模块进行自动交互
DISPLAY=1 SSH_ASKPASS="${ssh_passphrase_name}" ssh-add ${ssh_key_path} < /dev/null
ssh-add -l

env_var=(SSH_AGENT_PID SSH_AUTH_SOCK)
declare -A output_dict

for i in ${env_var[*]};
do
    output_dict[${i}]=`env|grep ${i}|awk -F '=' '{print $2}'`
done




output_func(){
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

output_func  > ${shell_output_json}
