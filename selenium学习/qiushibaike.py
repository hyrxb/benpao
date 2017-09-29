#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import random
import re
page = 1

url = 'http://www.qiushibaike.com/hot/page/' + str(page)


user_agents = [
                 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
		 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
		 'User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
		 'User-Agent,Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
		 'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
		 'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
		 'User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
              ]

user_agent = random.choice(user_agents)

headers = {'User-Agent':user_agent}




def getContent(html):
	pattern = re.compile(
		'<div.*?author.*?<a href=\"(.*?)\".*?<img src=\"(.*?)\".*?<a.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?">(.*?)</div>',re.S)
	items = re.findall(pattern,html)
	for item in items:
		print item[0],item[1],item[2]


try:
	request = urllib2.Request(url,headers=headers)
	response = urllib2.urlopen(request)
	html =  response.read().decode("utf-8")
	getContent(html)
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason