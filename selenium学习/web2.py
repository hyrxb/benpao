#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

import time

driver = webdriver.Firefox()

first_url =  'http://www.baidu.com'

print "now access %s" %(first_url)

driver.get(first_url)

second_url = 'http://news.baidu.com'

print 'now access %s' %(second_url)

driver.get(second_url)
#后退
print "back to %s" %(first_url)
driver.back()

print "forward to %s" %(second_url)
#前进
driver.forward()
driver.quit()
