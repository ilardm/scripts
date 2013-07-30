#!/usr/bin/python
# -*- coding: utf-8 -*-

import time, os
while 1:
	ntime=time.localtime()
	print "%s/%s/%s %s:%s:%s"%(ntime.tm_year,
							   ntime.tm_mon,
							   ntime.tm_mday,
							   ntime.tm_hour,
							   ntime.tm_min,
							   ntime.tm_sec)
	os.system("lynx -dump \"http://aid.ntl.nnov.ru/rip.php?a=set\"")
	time.sleep(240)
