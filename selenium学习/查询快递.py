#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import random

# http://www.kuaidi100.com/query?type=ems&postid=1033291133826&id=1&valicode=&temp=0.2661384065187702

#通过快递100接口查询快递
url = 'http://www.kuaidi100.com/query'

user_agents = [
                 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
		 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
		 'User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
		 'User-Agent,Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
		 'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
		 'User-Agent, Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
		 'User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
              ]

#随机选取一个user_agent
user_agent = random.choice(user_agents)

#设置header头
headers = {'User-Agent':user_agent,'Referer':'http://www.kuaidi100.com'}

values = {}

values['type'] = 'ems'
values['postid'] = 1033291133826
values['id'] = 1
values['valicode'] = ''
values['temp'] = 0.2661384065187702

data = urllib.urlencode(values)
url = url + "?" + data 

request = urllib2.Request(url,'',headers)

response = urllib2.urlopen(request)

print response.read()

