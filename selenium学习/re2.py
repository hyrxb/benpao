#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

pattern = re.compile(r'world')

match = re.search(pattern,'hello world!')

if match:
		print match.group()
		