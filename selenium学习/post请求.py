#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
values = {'appkey':'1016903103@qq.com','type':'sfexpress','number':931658943036}
data = urllib.urlencode(values)


url  =  'http://api.jisuapi.com/express/query'

request  =urllib2.Request(url,data)

response = urllib2.urlopen(request)

print response.read()
