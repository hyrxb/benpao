#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

request = urllib2.Request('http://www.baidu.com')

try:
	urllib2.urlopen(request)
except urllib2.URLError,e:
	print e.reason

