#!/usr/bin/python
# -*- coding:utf8 -*-
# demo http://www.cnblogs.com/melonjiang/p/5342505.html

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

    def testHkeys(self):
        print self.__conn.hexists("dd","a1")

    def testDel(self):
        print self.__conn.hdel("dd","a1")

    def testHincrby(self):
        print self.__conn.hincrby("dd","aa",amount=2)

    def testLpush(self):
        self.__conn.lpush("list_name",2)
        self.__conn.lpush("list_name",3,4,5)
        print self.__conn.lrange("list_name",0,-1)

    def testRpush(self):
        self.__conn.rpush("list_name",7,8,9)
        print self.__conn.lrange("list_name",0,-1)

    def testLlen(self):
        print self.__conn.llen('list_name')

    #在name对应的list列表的某一个值的前或者后插入一个新值
    def testLinsert(self):
        self.__conn.linsert('list_name','BEFORE',2,"SS")
        print self.__conn.lrange("list_name",0,-1)

    def testLset(self):
        self.__conn.lset("list_name",0,"bbb")
        print self.__conn.lrange("list_name",0,-1)

    def testSadd(self):
        self.__conn.sadd("set_name","aa")
        self.__conn.sadd("set_name","aa","bb")

    def testSmembers(self):
        print self.__conn.smembers("set_name")

    def testScard(self):
        print self.__conn.scard("set_name")

    def testSdiff(self):
        self.__conn.sadd("set_name","aa","bb")
        self.__conn.sadd("set_name1","bb","cc")
        self.__conn.sadd("set_name2","bb","cc","dd")
        print self.__conn.sdiff("set_name","set_name1","set_name2")

    def testSinter(self):
        self.__conn.sadd("set1","aa","bb")
        self.__conn.sadd("set2","bb","cc")
        self.__conn.sadd("set3","bb","cc","dd")
        print self.__conn.sinter("set1","set2","set3")


    def testZadd(self):
        self.__conn.zadd('zset_name',"a1",6,"a2",2,"a3",5)

    #获取有序集合内元素的数量
    def testZcard(self):
        print self.__conn.zcard("zset_name")

    #获取有序结果中分数在[min,max]之间的个数
    def testZcount(self):
        print self.__conn.zcount("zset_name",1,5)

    #自增有序集合内value对应的分数
    def testZincrby(self):
        self.__conn.zincrby("zset_name","a1",amount=2)


redisDemo2 = RedisDemo02()
# redisDemo2.testString()
# redisDemo2.redis_reads()
# redisDemo2.testIncr()
# redisDemo2.testAppend()
# redisDemo2.testHash()
# redisDemo2.testHgetAll()
# redisDemo2.testHmset()
# redisDemo2.testHlen()
# redisDemo2.testHkeys()
# redisDemo2.testHincrby()
# redisDemo2.testLpush()
# redisDemo2.testRpush()

# redisDemo2.testLlen()
# redisDemo2.testLinsert()
# redisDemo2.testLset()
# redisDemo2.testSadd()
# redisDemo2.testSmembers()
# redisDemo2.testSdiff()
# redisDemo2.testScard()
# redisDemo2.testSinter()

redisDemo2.testZadd()
redisDemo2.testZcard()
redisDemo2.testZcount()
redisDemo2.testZincrby()









