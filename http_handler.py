#!/usr/bin/env python

# -*- codingLutf-8 -*-

import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHanfler  = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
