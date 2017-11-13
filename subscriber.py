#!/usr/bin/env python
# -*- coding:utf8 -*-

from monitor1 import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()()
while True:
    msg = redis_sub.parse_response()
    print msg

