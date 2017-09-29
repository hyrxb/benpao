#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2

values = {}
values['sign'] = '08c1d5'
values['id'] = 25761813
data = urllib.urlencode(values)
url = 'http://api.3g.club.xywy.com/dev/ques_mi_detail.php' + "?" + data

#print url
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()

