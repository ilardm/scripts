#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

fetcher = urllib2.urlopen("http://checkip.dyndns.org/")
addr=fetcher.read()
print "rip:",addr.split(":")[-1].split("<")[0].replace(" ", "")
