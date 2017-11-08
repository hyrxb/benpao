#!/usr/bin/env python
#-*- coding:utf8 -*-

# python 连接 Redis
#
# 1）前往 redis-py 下载发布版本 release，最新发布版本： redis-py-2.8.0.zip
#
# wget https://github.com/andymccurdy/redis-py/archive/2.8.0.tar.gz
#
# 2）解压 redis-py-2.8.0.zip： unzip  redis-py-2.8.0.zip， 安装：  sudo python setup.py install
#
# 3）验证安装成功：
#
# # python
# >>> import redis
# >>>
#
#
# redis 设置密码
#
# a） 修改配置文件
#
# viim  redis.conf
#
# b） 添加一行
#
# requirepass '123456'
#
# c）重启redis服务
#
# /usr/local/bin/redis-server  /etc/redis.conf
#
# d）登陆 redis-cli
#
# $ redis-cli
# 127.0.0.1:6379> set foo bar
# (error) NOAUTH Authentication required.        // 设置了密码，操作没有权限
# 127.0.0.1:6379> help auth                               // 查看auth命令帮助
#   AUTH password
#   summary: Authenticate to the server
#   since: 1.0.0
#   group: connection
#
#
# 127.0.0.1:6379> auth '123456'                       // 输入密码，权限认证
# OK
# 127.0.0.1:6379> set foo bar                           // 密码权限认证成功后，可以操作
# OK
# 127.0.0.1:6379> get foo
# "bar"
#
#
# redis-cli 远程连接
#
# $ redis-cli --help
# redis-cli 2.8.12
# Usage: redis-cli [OPTIONS] [cmd [arg [arg ...]]]
#   -h <hostname>      Server hostname (default: 127.0.0.1).
#   -p <port>          Server port (default: 6379).
#   -s <socket>        Server socket (overrides hostname and port).
#   -a <password>      Password to use when connecting to the server.
#
#
# redis-cli 远程连接命令
#
# redis-cli -h 123.10.78.100 -p 6379 -a '123456'
#
# 注意：为了安全，redis不要用默认端口（6379），强烈推荐使用密码（requirepass 'xxx'），否则很容易被别人访问！

import redis

r = redis.StrictRedis(host='localhost',port=6300,db=0,password='123456')

r.set('test','001')

print r.get('test')
