#!/usr/bin/env python
# -*- coding:utf8 -*-

# 下载python中MongoDB的驱动程序
#
# pip install pymongo
#
# 然后确保MongoDB已经安装且可以正常运行，去官网下载相应版本：https://www.mongodb.com/
#
# mkdir -p /home/tools
# cd/home/tools
# wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.2.tgz
#
# 解压文件并修改目录名
#
#
# tar -zxvf mongodb-linux-x86_64-3.4.2.tgz
# mv mongodb-linux-x86_64-3.4.2 mongodb3.4.2
# ln -s mongodb_3.4.2 mongodb
#
# MongoDB 的可执行文件位于 bin 目录下，所以可以将其添加到 PATH 路径中
#
# export PATH=/home/tools/mongodb/bin:$PATH
#
# MongoDB的数据存储在data目录的db目录下，但是这个目录在安装过程不会自动创建，所以你需要手动创建data目录，并在data目录中创建db目录。
#
# mkdir -p /data/db
#
# 在mongo安装目录中的bin目录执行mongod命令来启动mongdb服务
#
# ./mongod --dbpath /data/db
#
# 如果想进入MongoDB后台管理
#
# ./mongo


from pymongo import MongoClient

conn = MongoClient("127.0.0.1",27017)

db = conn.mydb

db.my_test.insert({"name":"zhangshan","age":18})
db.my_test.save({"name":"jack","age":20})

#插入多条数据

users = [{"name":"lucy","age":10},{"name":"davae","age":18}]

db.my_test.insert(users)

for i in db.my_test.find():
    print (i)

for i in db.my_test.find({"name":"zhangshan"}):
    print(i)

print db.my_test.find_one({"name":"zhangshan"})



#更新数据

db.my_test.update({"name":"zhangshan"},{'$set':{"age":20}})

print db.my_test.find_one({"name":"zhangshan"})

#db.my_test.remove({"name":"zhangshan"})

id =db.my_test.find_one({"name":"zhangshan"})["_id"]

print "+"*50 + "华丽的分割线" +"+"*50

print id

db.my_test.remove(id)

print db.my_test.find_one({"name":"zhangshan"})

#mongodb条件操作

#    (>)  大于 - $gt
#    (<)  小于 - $lt
#    (>=)  大于等于 - $gte
#    (<= )  小于等于 - $lte


for i in db.my_test.find({"age":{"$gt":10}}):
    print i


print "+"*50 + "华丽的分割线" +"+"*50

#排序

for i in db.my_test.find().sort([("age",1)]):
    print i

#limit 和skip

for i in db.my_test.find().skip(2).limit(6):
    print i

print "+"*50 + "华丽的分割线 找出age是20,30,35的数据" +"+"*50


#找出age是20,30,35的数据

for i in db.my_test.find({"age":{"$in":(20,30,35)}}):
    print i

#找出年龄是20或者18的数据
print "+"*50 + "华丽的分割线 找出年龄是20或者18的数据" +"+"*50

for i in db.my_test.find({"$or":[{"age":20},{"age":35}]}):
    print i

