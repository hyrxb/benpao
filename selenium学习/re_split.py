#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

pattern = re.compile(r'\d+')

print re.split(pattern,'one1two2three3four4')
