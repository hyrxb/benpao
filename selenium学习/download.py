#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

from bs4 import BeautifulSoup
 
def download(url,num_retries=2):
 	print 'Downloading:',url
 	try:
 		html = urllib2.urlopen(url).read()
 	except urllib2.URLError as e:
 		print 'Download error:',e.reason
 		html = None
 		if num_retries > 0:
 			if hasattr(e,'code') and 500 <= e.code < 600:
 				return download(url,num_retries -1)
 	return html


def download2(url,user_agent='wswp',num_retries=2):
	print 'DOwnloading:',url
	headers = {'User-agent':user_agent}
	request.urllib2.Request(url,headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Download error:',e.reason
		html = None
		if num_retries > 0:
			if hasattr(e,'code')  and 500 <=e.code < 600:
				return download(url,user_agent,num_retries-1)
		return html



html = download('http://www.xiaomi.com')

soup = BeautifulSoup(html,"lxml")

div =  soup.find(attrs={'id':"J_navCategory"})
span = div.find(attrs={'class':'text'})
print span.text