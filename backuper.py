#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time

argc=len(sys.argv)
argv=sys.argv

#print argc, argv

# common functions
def arrayContains( _what, _where ):
    for i in _where:
        if ( i==_what ):
            return True
    
    return False

def help():
    version="Version: 1.0"
    
    general="""backuper is script which keeps your data under git repository
in current implementation it doesn't suppor another git repositories under backup repository
"""
    usage="""Use:
\tbackuper.py -h\t-\tmanual backup repos listed in ~/.backuper/repos.list
\tbackuper.py <list_file>\t-\tmanual backup repos listed in <list_file>

\tadd backuper.sh in cron to set up auto backup listed in ~/.backuper/repos.list

\t<list_file> is plain text file which contains full path to backup git repository
\tyou can create it by execution cmd 'cd <path_to_repo>; pwd >> ~/.backuper/repos.list'
"""
    
    author="""Author: Ilya Arefiev <arefiev.id@gmail.com> (c) 2010
Licence: GPLv3
"""
    print general
    print usage
    print version
    print author

if ( argc>1 and ( argv[1]=="-h" or argv[1]=="--help" ) ):
    help()
    sys.exit(0)

if ( not os.path.exists( os.path.expanduser("~/.backuper/logs/") ) ):
    os.makedirs( os.path.expanduser("~/.backuper/logs/") )
    
# read backup places
repos=[]
confPath=""
processed=0
auto=True

try:
    if ( argc!=1 ):
        confPath=argv[1]
        auto=False
    else:
        confPath=os.path.expanduser("~/.backuper/repos.list")
        
    fd=file(confPath)
    
    try:
        while ( True ):
            repos.append( fd.next().replace("\n","") )
    except StopIteration:
        fd.close()

    #print repos
    
except IOError:
    print "oops. no config file at '%s'"%confPath
    sys.exit(1)

# start work with repos
for repo in repos:
    if ( repo=="" ):
        continue

    now=time.localtime()
    date="%04d%02d%02d %02d%02d%02d"%( now.tm_year,
                                       now.tm_mon,
                                       now.tm_mday,
                                       now.tm_hour,
                                       now.tm_min,
                                       now.tm_sec )
                    
    print "will work with '%s' @ %s"%(repo,date)
    waitingForNew=False
    waitingForDelete=False
    
    try:
        os.chdir(repo)

        dirList=os.listdir(".")
        if ( arrayContains ( ".git", dirList ) and os.path.isdir(".git") ):
            newObjects=[]
            deleteObjects=[]
            modifiedObjects=[]
            
            pipe=os.popen("git status")

            try:
                while ( True ):
                    line=pipe.next().replace("\n", "")

                    # new objects
                    if ( line.find("Untracked files:")!=-1 ):
                        print "will search for newObjects"
                        
                        waitingForDelete=False
                        waitingForNew=True
                        
                    # delete (if contains deleted) objects
                    if ( line.find("Changed but not updated:")!=-1 ):
                        #print "will search for deleteObjects"

                        waitingForNew=False
                        waitingForDelete=True

                    # parse git-log to commit changes
                    if ( line.find("#")==0 ):
                        if ( waitingForNew ):
                            line=line.replace("#", "").strip()
                            if ( os.path.isfile(line) or os.path.isdir(line) ):
                                newObjects.append(line)

                        if ( waitingForDelete ):
                            if ( line.find("deleted")!=-1 ):
                                line=line.replace("#", "").replace("deleted:", "").strip()
                                deleteObjects.append(line)
                            if ( line.find("modified")!=-1 ):
                                line=line.replace("#", "").replace("modified:", "").strip()
                                modifiedObjects.append(line)
                        
            except StopIteration:
                pipe.close()

                print "new \t\t",newObjects
                print "deleted \t",deleteObjects
                print "modified \t",modifiedObjects

                print "will execute commands"

                for i in deleteObjects:
                    es=os.system("git rm \"%s\" > /dev/null"%i)

                    if ( es!=0 ):
                        print "rm '%s' exited with #%d"%(i,es)
                    
                for i in newObjects:
                    es=os.system("git add \"%s\" > /dev/null"%i)

                    if ( es!=0 ):
                        print "add '%s' exited with #%d"%(i,es)
                    
                now=time.localtime()
                date="%04d%02d%02d %02d%02d"%( now.tm_year,
                                               now.tm_mon,
                                               now.tm_mday,
                                               now.tm_hour,
                                               now.tm_min )

                print "will commit canges"

                msg=""
                if ( auto ):
                    msg="auto commit at %s"%date
                else:
                    msg="manual commit at %s"%date

                # FIXME: cyrillic filenames not commited
                os.system("git add .")  # temporary workaround
                
                es=os.system("git commit -am \"%s\" > /dev/null"%msg)

                now=time.localtime()
                date="%04d%02d%02d %02d%02d%02d"%( now.tm_year,
                                                   now.tm_mon,
                                                   now.tm_mday,
                                                   now.tm_hour,
                                                   now.tm_min,
                                                   now.tm_sec)
                    
                print "backup exit status #%d @ %s\n"%(es,date)

                processed+=1

        else:
            print "no .git/"
        
    except OSError:
        print "no such dir ('%s')?"%repo
        pass

if ( processed!=0 ):
    print "processed %d repos"%processed
else:
    print "no repos found"
