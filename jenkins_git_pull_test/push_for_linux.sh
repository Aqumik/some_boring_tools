#!/bin/bash
#
PATHH="$(dirname $0)"
DATE=`date +%m%d%H%M`
echo "BUILD_NUMBER" :: $BUILD_NUMBER 
echo "BUILD_ID" :: $BUILD_ID 
echo "BUILD_DISPLAY_NAME" :: $BUILD_DISPLAY_NAME 
echo "JOB_NAME" :: $JOB_NAME 
echo "JOB_BASE_NAME" :: $JOB_BASE_NAME 
echo "BUILD_TAG" :: $BUILD_TAG
echo "EXECUTOR_NUMBER" :: $EXECUTOR_NUMBER
echo "NODE_NAME" :: $NODE_NAME
echo "NODE_LABELS" :: $NODE_LABELS
echo "WORKSPACE" :: $WORKSPACE
echo "JENKINS_HOME" :: $JENKINS_HOME
echo "JENKINS_URL" :: $JENKINS_URL
echo "BUILD_URL" ::$BUILD_URL
echo "JOB_URL" :: $JOB_URL
echo "我是挖坑作者" :: $BUILD_USER
echo "挖坑作者邮箱" :: $BUILD_USER_EMAIL 
echo "挖坑作者ID" :: $BUILD_USER_ID 

FILE_PATH=$WORKSPACE
echo '你好你好 ！！！！！'$FILE_PATH






<<'COMMENT'
	工作思想
    判断gitlab.cucucu.cn加密认证是否存在于known_host
	1、判断是否有 推送文件夹
	2、进入文件夹
	3、判断文件夹是否进行了git初始化
		(判断条件)若没有进行git init则进行初始化，若已进行git初始化
	5、判断最新远程和本地的commit的md5是否一致
		(判断条件)不一致，更新远程分支到本地；一致，下一步
	6、清空目录，复制jenkins的工作目录的文件到 推送文件夹
	7、推送动作。。。

	当前问题：
	a.如何获取git分支名字
	b.如何保证git指针名字
	c.如何知道远程仓库ssh链接

COMMENT

worksapce_path=$WORKSPACE
worksapce_name=${worksapce_path##*/}
gitlab_file_dic=/tmp/gitlab
push_path=${gitlab_file_dic}/${worksapce_name}_push
push_file_name=${worksapce_name}_push
#用户名变量为jenkins的用户
user_name=$BUILD_USER

echo "脚本输出作者：${user_name}"
user_email=${user_name}'@cucucu.com'
remote_branch_name=main
local_branch_name=main
repository_name=origin
git_file=".git/"
git_ssh_url='git@gitlab.cucucu.cn:tu/push_test.git'

# commit 内容，是否可以从jenkins外部传入？
com_mes="推送测试1"

#ssh_agent部分
ssh_private_path="/tmp/tu"
ssh_private_key="your password\r"
echo $worksapce_path
echo '推送路径为-----'$push_path
echo $user_email

#ssh 公钥部分
#请确认用于提交到gitlab的密钥加密类型
ssh_key_encryption_type='ecdsa-sha2-nistp256'
ssh_know_host="gitlab.cucucu.cn"
ssh_know_host_command=`cat ~/.ssh/known_hosts |grep -wc ${ssh_know_host}`

#用于检查jenkins的用户目录下的 know_host是否有 gitlab.cucucu.cn
#获取到后返回其加密方式
ssh_agent_know_hosts_check(){
	if [[ ${ssh_know_host_command} -gt 0 ]];then
		ssh_key_encryption_type_now=`cat ~/.ssh/known_hosts |grep -w ${ssh_know_host} |awk -F ' ' '{print $2}'`
		echo "gitlab已存在~/.ssh/known_hosts ，以认证密钥加密方式为${ssh_key_encryption_type_now}"
	elif [[ ${ssh_know_host_command} -eq 0 ]];then
        	ssh-keyscan -t ${ssh_key_encryption_type} ${ssh_know_host} >> ~/.ssh/known_hosts
        	echo "gitlab不存在~/.ssh/known_hosts ，脚本已为你添加...当前认证密钥加密方式为${ssh_key_encryption_type}"
        else
        	echo "known_hosts有问题，请检查......"
        	exit 2
        fi

}

ssh_agent_init(){
	eval $(/usr/bin/ssh-agent -s)
	/usr/bin/expect <<-EOF
	spawn ssh-add	${ssh_private_path}
	expect "Enter passphrase for ${ssh_private_path}:"
	send ${ssh_private_key}
	interact
	expect eof
	EOF
	pid=$(env |grep -E SSH_AGENT_PID |awk -F '=' '{print $2}')
#	git clone git@github.com:Aqumik/learngit.git
	echo -e '\n'
	echo ${pid}
	echo `ssh-add -l`
	
}


#问题1：如何传入分支名字以及指针名字？？
#获取当前分支hash
check_branch_hash(){
        branch_name=`git rev-parse --abbrev-ref HEAD`
        echo "当前分支名"${branch_name}
        local_branch_hash=`git rev-parse HEAD`
        echo "当前本地分支Hash"${local_branch_hash}
        echo "更新远程分支....."
        git remote update
        echo "获取远程分支Hash"
        remote_branch_hash=`git rev-parse origin/main`
        echo "远程分支Hash"${remote_branch_hash}
        if [[ ${local_branch_hash} == ${remote_branch_hash} ]];then
                echo "最新commit的Hash一致"
        else
                echo "!!!!当前本地分支与远程分支commit的Hash不一致!!!"
                echo "将会更新远程分支到本地"
                sleep 5
                #考虑到本地commit失败，此处选择的是回退本地commit与远程分支的commit一致。
                git reset --hard ${repository_name}/${remote_branch_name}
                git pull ${repository_name} ${remote_branch_name}
                echo '....................'
                check_branch_hash
        fi
}


#git提交人信息
git_commit_user(){
	cd ${push_path}
	echo "修改提交人为当前登录账户"
	git config --local user.name ${user_name} 
	echo "修改提交邮箱"
	git config --local user.email ${user_email}
}

git_commit_action(){
	
	echo "清空推送目录文件"
	rm -r  ${push_path}/*
	echo "复制构建到推送目录"
	cp -r ${worksapce_path}/* ${push_path}
	cd ${push_path}
	pwd
	echo "更新分支内容"
	git pull ${repository_name} ${remote_branch_name}
	echo "提交内容"
	git add ./
	#read -p "请输入提交信息: " com_mes
	echo "提交信息"
	git commit -a -m "${com_mes}"
	echo "推送到远程仓库"
	git push ${repository_name} ${remote_branch_name}
}

#初始化文件
#如何传入git仓库变量？？？？？
#返回值1，有该文件并有本地git库
#返回值2，有该文件，但没有本地git库
#返回值3，该文件不存在
pushfile_init_action(){

	if [ -d ${push_path} ]; then
		echo "推送目录已存在"
		#进入具体 推送目录 判断其下是否有 ./git
		cd ${push_path}
		if [[ -d ${git_file} ]]; then
			echo "有此文件，git已初始化"
			return	1
		else
			echo '此文件不存在'
			return	2
		#git_init_action
		fi
		
	else
		echo "${push_path} 推送目录不存在，将会创建...."
		
		#mkdir ${push_path}
		#git_init_action
		return 3
	fi

}


git_init_action(){
	return_function=`pushfile_init_action`
	return_num=$?
	echo ${return_num}
	if [[ return_num -eq 1 ]]; then
		echo "有此文件，git已初始化"
	elif [[ return_num -eq 2 ]]; then
		echo "有此文件，但是没有本地仓库"
		cd ${push_path}
		git init
		git checkout -b ${local_branch_name}
		git remote add ${repository_name} ${git_ssh_url} 
		git pull ${repository_name} ${remote_branch_name}
		git checkout -b ${local_branch_name} ${repository_name}/${remote_branch_name}
		git 
	else
		echo "没有此文件"
		cd ${gitlab_file_dic}
        #ssh-keyscan -t ecdsa-sha2-nistp256 gitlab.cucucu.cn >> ~/.ssh/known_hosts
		echo `ssh-add -l`
		echo `pwd`
		echo "git clone ${git_ssh_url} ${push_file_name}"
        cat ~/.ssh/known_hosts
		git clone ${git_ssh_url} ${push_file_name}
	fi
}






#主体函数
main(){
	ssh_agent_know_hosts_check
	#进入存放 推送目录 文件夹进行判断
	ssh_agent_init
	cd ${gitlab_file_dic}
	pushfile_init_action
	git_init_action
	git_commit_user
	check_branch_hash
	git_commit_action
	kill ${pid}
	echo "has been killed ssh-agent ${pid}"	
}

main