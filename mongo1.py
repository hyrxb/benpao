#!/usr/bin/env python
#-*- coding:utf8 -*-

# sudo apt-get install mongodb
# service mongodb start
# service mongodb stop
#
# pymongo
#
# 安装 wget https://pypi.python.org/packages/source/p/pymongo/pymongo-2.6.tar.gz
#
# tar zxvf pymongo-2.6.tar.gz
#
# cd pymongo-2.6
#
# sudo python setup.py build
#
# sudo python setup.py install

import pymongo

import random

_DB = 'school'
_TABLE = 'student'

HOST = "127.0.0.1"
PORT = 27017

conn = pymongo.Connection(HOST,PORT);

db = conn[_DB]
table = db[_TABLE]

table.save({"id":2,"name":"homer","age":18})

for id in range(2,10):
    name = random.choice(['it','homer','sunboy','yangguang'])
    age = random.choice([10,20,30,40,50,60])
    table.insert({'id':id,'name':name,'age':age})

cursor = table.find()
for user in cursor:
    print user
