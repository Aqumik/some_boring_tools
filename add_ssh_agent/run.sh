#!/bin/bash
#eval `/usr/bin/ssh-agent bash`
eval $(/usr/bin/ssh-agent -s)


ls_date=`date +%Y-%m-%d`

#/usr/bin/bash -i

echo '...............'
#ssh-agent bash


# send 你的私钥密码
/usr/bin/expect <<-EOF
spawn ssh-add  /home/aqumik/zhi
expect "Enter passphrase for /home/aqumik/zhi:"
send "cde3\r"
interact
expect eof
EOF
#
#echo ${ls_date}
pid=$(env |grep -E SSH_AGENT_PID |awk -F '=' '{print $2}')


git clone git@github.com:Aqumik/learngit.git

echo -e '\n'
echo ${pid}
kill ${pid}
echo "has been killed ${pid}"
#/usr/bin/bash -i
# ssh-agent属于交互式，ssh-agent启动一个会话，当他完成时用户会话后就结束，因此在ssh-agent的任何命令需要注销后执行。
# 个人理解为重新建立会话
