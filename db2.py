#!/usr/bin/env python
# -*- coding:utf8 -*-

import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="python")

cursor = db.cursor()

cursor.execute("SELECT * FROM memory")

result = cursor.fetchall()

for row in result:
    # print row[0],row[1]
    print ','.join( [ str(row[0]), str(row[1]) ] )

cursor.close()
