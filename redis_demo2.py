#!/usr/bin/python
# -*- coding:utf8 -*-

import sys

import redis

class RedisDemo02(object):

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1',port=6300,db=0,password='123456')

    def redis_reads(self):
        self.__conn.flushdb()
        self.__conn.set('foo','bar')
        print self.__conn.get('foo')
        self.__conn.set('blog','ithomeself.__conn.net')
        self.__conn.set('name','zhangsan')
        print(self.__conn.getrange('name',0,3))
        self.__conn.mset(name1='zhangsan',name2='lisi')
        self.__conn.mset({"name3":"lisi","name4":"jack"})
        print self.__conn.mget("name1","name2")
        print self.__conn.mget(['name3','name4'])

    def testString(self):
        self.__conn.set("name","zhangsan")
        self.__conn.getset("name5","jack")
        self.__conn.setrange("name5",1,"z")
        print(self.__conn.get("name5"))
        self.__conn.setrange("name5",6,"zzzzzzz")
        print(self.__conn.getrange("name",0,3))
        print self.__conn.get("name5")


    def testIncr(self):
        print self.__conn.incr("mount",amount=2)
        print self.__conn.incr("mount")
        print self.__conn.get("mount")

    def testAppend(self):
        self.__conn.set('name2',"zhangsan")
        print self.__conn.get("name2")
        self.__conn.append("name2","list")
        print self.__conn.get("name2")

    def testHash(self):
        self.__conn.hset("dict_name","a1","aa")
        print self.__conn.hget("dict_name","a1")

    def testHgetAll(self):
        self.__conn.hset("dict",'name','jack')
        self.__conn.hset("dict","age",20)
        print self.__conn.hgetall("dict")

    def testHmset(self):#设置多个值
        dict = {"a1":"aa","b1":'bb'}
        self.__conn.hmset("dd",dict)
        print self.__conn.hget("dd","a1")
        print self.__conn.hget("dd","b1s")

    def testHmget(self):
        li = ["a1","b1"]
        print self.__conn.hmget("dd",li)
        print self.__conn.hmget("dd","a1","b1")

    def testHlen(self):
        print self.__conn.hlen("dd")
        print self.__conn.hkeys("dd")
        print self.__conn.hvals("dd")


redisDemo2 = RedisDemo02()
# redisDemo2.testString()
# redisDemo2.redis_reads()
# redisDemo2.testIncr()
# redisDemo2.testAppend()
# redisDemo2.testHash()
redisDemo2.testHgetAll()
redisDemo2.testHmset()
redisDemo2.testHlen()



