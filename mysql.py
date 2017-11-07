#!/usr/bin/env python
#-*- coding:utf8 -*-

'''

安装MySQL-python

要想使python可以操作mysql 就需要MySQL-python驱动，它是python 操作mysql必不可少的
模块。

下载地址：https://pypi.python.org/pypi/MySQL-python/

下载MySQL-python-1.2.5.zip 文件之后直接解压。进入MySQL-python-1.2.5目录:

>>python setup.py install

测试,进入

ipython

In [4]: import MySQLdb

如果没有报错，则安装成功


CREATE TABLE `memory` (
  `memory` varchar(20) DEFAULT '',
  `time` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8

'''

import time

import MySQLdb as mysql


db = mysql.connect(user="root",passwd="123456",db="python",host="localhost")

db.autocommit(True)

cur = db.cursor()

# print cur

def getMem():
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    mem_use = total-free-buffers-cache
    t = int(time.time())
    sql = "insert into memory (memory,time) value(%s,%s)" %(mem_use/1024,t)
    cur.execute(sql)
    print mem_use/1024


while True:
    time.sleep(1)
    getMem()



