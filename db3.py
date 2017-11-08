#!/usr/bin/env python
# -*- coding:utf8 -*-

import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="python")

cursor = db.cursor()

cursor.execute("Select * from memory limit 10")

result = cursor.fetchall()

for row in result:
    print ' ,' .join([str(row[0]),str(row[1])])

