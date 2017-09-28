#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://passport.kuaibo.com/login/?referrer=http')
driver.find_element_by_id("user_name").clear()
driver.find_element_by_id("user_name").send_keys("usernames")
driver.find_element_by_id("user_pwd").clear()
driver.find_element_by_id("user_pwd").send_keys("user_pwd")
driver.find_element_by_id("dl_an_submit").click();
driver.quit()

