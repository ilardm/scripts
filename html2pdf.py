#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

argc=len(sys.argv)
argv=sys.argv


if ( argc>1 ):
    url = "http://pdfmyurl.com?url="+argv[1].replace("\"", "")
    outfile=argv[1].replace("\"", "").replace("/", "_")+".pdf"
    os.system( "wget -O %s %s"%(outfile, url) )
else:
    print "where is url?"
