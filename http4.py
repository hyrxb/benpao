#!/usr/bin/env python
# -*- coding:utf8 -*-
#__author__:benpao
#  BeautifulSoup demo https://www.cnblogs.com/yizhenfeng168/p/6979339.html
# http://www.cnblogs.com/yizhenfeng168/tag/python%E7%88%AC%E8%99%AB/

from bs4 import  BeautifulSoup

import urllib2

url = "http://www.136book.com/huaqiangu/"

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}

req = urllib2.Request(url,headers=headers)

res = urllib2.urlopen(req)

html = res.read()

# print html


bs4 = BeautifulSoup(html,'html.parser')

for node in  bs4.select("div.box1 li a"):
    print node["href"]