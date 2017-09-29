#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
	'stuid':'201200121012'
	'pwd':'123'
	})

loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'

result = opener.open(loginUrl,postdata)

cookie.save(ignore_discard=True,ignore_expires=True)

gradeUrl = 'http://jwxt.stu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'

result = opener.open(gradeUrl)

print result.read()

