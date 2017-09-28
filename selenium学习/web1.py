#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://m.mail.10086.cn')
print 'height : 800 ,width:480 '
driver.set_window_size(480,800)
driver.quit()