#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, string

# === constants ===============================================================

argv = sys.argv
argc = len(argv)

SWGROUPS = {   "editors":
                [   "vim-gtk"
                  , "emacs23-gtk"
                ]
             , "dictionaries":
                [   "ispell"
                  , "iamerican"
                  , "irussian"
                ]
             , "development":
                [   "make"
                  , "cmake"
                  , "g++"
                  , "clang"
                  , "gdb"
                  , "valgrind"
                  , "libqt4-dev"
                  , "exuberant-ctags"
                  , "doxygen"
                  , "git"
                  , "qgit"
                  , "mercurial"
                ]
             , "util":
                [   "mc"
                  , "tmux"
                  , "pmount"
                  , "htop"
                  , "pbzip2"
                  , "unrar"
                  , "ntpdate"
                  , "vsftpd"
                ]
             , "network":
                [   "curl"
                  , "lynx"
                  , "tcpdump"
                  , "rtorrent"
                ]
             , "multimedia":
                [   "gstreamer0.10-plugins-good"
                  , "gstreamer0.10-plugins-ugly"
                  , "mplayer"
                  , "sox"
                  , "libsox-fmt-all"
                ]
             , "X":
                [   "fluxbox"
                  , "conky"
                  , "xxkb"
                  , "xinit"
                ]
           }

OPTIONS = {   "dry": False
            , "verbose": False
            , "help": None
            , "target": SWGROUPS.keys()
            , "targets": None
            , "show-target": None
          }

# === functions ===============================================================

def exec_cmd( cmd ):
    if ( OPTIONS["verbose"] ):
        print "execute cmd '%s'" % ( cmd )

    if ( OPTIONS["dry"] ):
        return 0
    else:
        return os.system( cmd )

def set_option( opt, val ):
    if ( not opt in OPTIONS.keys() ):
        return

    OPTIONS[opt] = val

def parse_arg( arg ):
    #print "parsing arg '%s'" % ( arg )

    arg = arg.replace( "--", "" )
    option = arg
    values = []

    if ( arg.find( "=" ) >= 0 ):
        option = arg.split( "=" )[0]
        values = arg.split( "=" )[1].split( "," )

    return ( option, values )

def process_arg( arg ):
    option = arg[0]
    values = arg[1]

    #print "processing arg '%s' with values" % ( option ), values

    if ( not option in OPTIONS.keys() ):
        print "unknown option '%s'" % ( option )

        sys.exit(0)

    if ( option == "verbose" ):
        set_option( option, True )

    if ( option == "help" ):
        print "known options:"

        for o in OPTIONS.keys():
            print "* --%s" % o

        sys.exit(0)

    if ( option == "dry" ):
        set_option( option, True )

    if ( option == "target" ):
        set_option( option, values )

    if ( option == "targets" ):
        print "known targets are:"

        for t in SWGROUPS.keys():
            print "* %s" % ( t )

        sys.exit(0)

    if ( option == "show-target" ):
        for t in values:
            if t in SWGROUPS.keys():
                print "packages in '%s':" % ( t )
                print SWGROUPS[t]
            else:
                print "unknown target '%s'" % ( t )

        sys.exit(0)

# === body ====================================================================

# --- check argumemts ---------------------------------------------------------
for iarg in xrange( 1, argc ):
    arg = parse_arg( argv[iarg] )
    process_arg( arg )

# --- perform installation ----------------------------------------------------
for g in OPTIONS["target"]:
    print "processing group '%s'" % ( g )

    cmd = "apt-get install -y "

    for p in SWGROUPS[g]:
        if ( OPTIONS["verbose"] ):
            print "'%s': '%s'" % ( g, p )

        cmd += (p + " ")

    es = exec_cmd( cmd )
    if ( not es == 0 ):
        print "error detected"

        sys.exit( es )
