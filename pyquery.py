#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests

from pyquery import PyQuery as pq

url = "http://www.baidu.com"

r = requests.get(url)
print r.text
print r.content

p = pq(r.text).find('a')

print p