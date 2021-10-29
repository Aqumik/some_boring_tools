# 需求情况

Gitalb自动提交代码时因为在linux终端下，每次使用密钥提交代码或远程服务器都需要重新加载密钥,并输入密码,此过程十分繁琐。
手动操作如下
```shell
	ssh-agent bash
	ssh-add /your_private_key
	Enter your private_key Password.....
```
## ssh-agent
查看ssh-agent相关工作原理可知，ssh-agent的工作是依赖于环境变量SSH_AUTH_SOCK和SSH_AGENT_PID的，不同用户，不同终端，只要没有和这两个环境变量配对的ssh-agent，这个agent进程就不可使用。要想使用某个agent，就必须在自己的shell中先设置好这两个环境变量；而后续的 `ssh-add` 查找当前环境变量SSH_AUTH_SOCK的值并发送添加请求给对应套接字。
`ssh-agent bash` 相当于重新另起一个bash环境，`ps`可以看到会添加多一个bash进程，并且查看当前bash的环境变量会多了 SSH_AUTH_SOCK和SSH_AGENT_PID 这两项，当会话退出，相关进程就会结束。
eval `ssh-agent` 启动会让ssh-agent工作在后台，终端退出变量消失，但是之前运行的ssh-agent仍然会存在于后台，脚本时运行要杀掉。


## 脚本情况
脚本使用了shell和expect混合，在脚本中暂时找不到成功运行`ssh-agent bash`方法，使用的是 eval `ssh-agent -s`，所以脚本在运行时会从环境变量中获取 SSH_AGENT_PID 的值，在任务完成后 杀掉 ssh-agent进程。

