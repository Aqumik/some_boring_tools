# 需求情况

Gitalb自动提交代码时因为在linux终端下，每次使用密钥提交代码或远程服务器都需要重新加载密钥,并输入密码
手动操作如下
```shell
	ssh-agent bash
	ssh-add /your_private_key
	Enter your private_key Password.....
```


