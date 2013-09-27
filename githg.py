#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys, string

ARGV = sys.argv
ARGC = len( ARGV )

GITLOG = "git log --name-status --no-merges --pretty=format:\"%h|_|%ad|_|%s\""
SINCE = ""
SINCEFOUD = False
DRYRUN = False

for i in xrange( ARGC ):
    print "argv[%d] '%s'" % ( i, ARGV[i] )

    if ( ARGC > 1 ):
        argv = ARGV[i]
        if ( argv.find( "--since" ) == 0 ):
            SINCE = argv.split( "=" )[1]
            print "since = '%s'" % SINCE
        if ( argv.find( "--dry" ) == 0 ):
            DRYRUN = True
            print "dryrun"

if ( len(SINCE) == 0 ):
    SINCEFOUD = True
    print "using full history"

def osexec( _cmd ):
    es_ = 0
    if ( not DRYRUN ):
        es_ = os.system( _cmd )
    else:
        print "dryrun"

    print "%d <== '%s'" % ( es_, _cmd )
    if ( not es_ == 0 ):
        raw_input()

# === body =====================================================================

CFD = os.popen( GITLOG )
LOG = CFD.read().split( "\n\n" )
LOG.reverse()
CFD.close()

#for i in LOG:
    #print "raw log:", i

#raw_input()

DLOG = []
for i in LOG:
    a = i.split( "\n" )

    rdm = a[0] # rev|_|date|_|msg
    rdm_ = rdm.split( "|_|" )

    files = []
    for j in a[1:]:
        files.append( j ) # A/M/D\tfilename

    e = {}
    e["rev"]    = rdm_[0]
    e["dt"]     = rdm_[1]
    e["msg"]    = rdm_[2]
    e["files"]  = files

    #print "entry:", e

    if ( not SINCEFOUD ):
        print "check if r'%s' is r'%s'" % ( SINCE, e["rev"])
        if ( SINCE.find( e["rev"] ) == 0 ):
            SINCEFOUD = True

    if ( SINCEFOUD ):
        DLOG.append( e )

#DLOG.reverse()
for i in DLOG:
    print "log:", i

    cmd = "git checkout -f %s" % i["rev"]
    #print "cmd '%s'" % cmd
    osexec( cmd )

    files = i["files"]
    if ( 0 == len( files ) ):
        # skip merges
        continue

    for j in files:
        if ( "" == j ):
            continue

        j_ = j.split( "\t" )
        
        m = j_[0]
        f = j_[1]

        cmd = ""
        if ( "A" == m ):
            cmd = "hg add %s" % f
        elif ( "D" == m ):
            cmd = "hg rm %s" % f

        if ( not "" == cmd ):
            #print "cmd '%s'" % cmd
            osexec( cmd )

    cmd = "hg ci -m \"%s\" -d \"%s\"" % ( i["msg"], i["dt"] )

    #print "cmd '%s'" % cmd
    osexec( cmd )
