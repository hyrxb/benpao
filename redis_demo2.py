#!/usr/bin/python
# -*- coding:utf8 -*-

import sys
import redis

def redis_reads():
    r = redis.Redis(host='127.0.0.1',port=6300,db=0,password='123456')
    r.flushdb()
    r.set('foo','bar')
    print r.get('foo')

    r.set('blog','ithomer.net')
    r.set('name','zhangsan')
    print(r.getrange('name',0,3))


redis_reads()