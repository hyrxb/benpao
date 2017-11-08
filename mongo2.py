#!/usr/bin/env python
# -*- coding:utf8 -*-

import pymongo #导入python mongo模块
import random

conn = pymongo.Connection("127.0.0.1",27017)

db = conn.test

for id in range(2,10):
    name =random.choice(['it','jack','lucy','kaokao','bi'])
    age = random.choice([10,20,30,40,50,60])
    db.student.insert({"id":id,"name":name,"age":age})

cursor=db.student.find()
for user in cursor:
    print user