#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

#print sys.argv[1]

s=""

os.system("ifconfig %s|grep bytes > /tmp/traf.tmp"%sys.argv[1])
f=open("/tmp/traf.tmp", "r")
s=f.next().replace("\n", "")
f.close()
os.system("rm -f /tmp/traf.tmp")

rx=s.split("(")[1].split(")")[0]
tx=s.split("(")[-1].split(")")[0]
print "r: %s\tt: %s"%(rx, tx)
