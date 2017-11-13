#!/usr/bin/env python
# -*- coding:utf8 -*-
# 注意文件名不能和库名一样

# demo http://www.cnblogs.com/kongzhagen/p/6402335.html

import urllib2

old_url = 'http://www.baidu.com'

req = urllib2.Request(old_url)

response = urllib2.urlopen(req)

print "Info():"

print response.info()