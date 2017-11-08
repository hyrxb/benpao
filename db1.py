#!/usr/bin/env python
# -*- coding:utf8 -*-

import MySQLdb

db = MySQLdb.connect("localhost","root","123456","python")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print "Database version:%s " % data
db.close()
