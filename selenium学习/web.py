#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print "last~~~~~~~~~~~~~~~~"

driver.maximize_window()
driver.quit()