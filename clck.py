#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, urllib2

argc=len(sys.argv)
argv=sys.argv


if ( argc>1 ):
    url = argv[1].replace("\"", "")
    fetcher = urllib2.urlopen("http://clck.ru/--?url="+url)
    short=fetcher.read()
    print short
else:
    print "where is url?"
