#!/bin/sh
if [ ! $1 ]; then
    echo "specify destination file";
    exit 1;
fi;

PID=`ps x | grep libflashplayer.so | grep -v grep | awk '{print $1}'`
FD=`lsof -p $PID | grep Flash | awk '{print $4}' | sed 's/u^//'`
cp /proc/$PID/fd/$FD "$1"
