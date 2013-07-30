#!/bin/bash

if [[ ! $1 ]]; then
    echo "no revision specified";
    exit 1;
fi;

DST_NAME="$(pwd | sed 's/.*\///')_$1";
hg archive -t tar -p "$DST_NAME/" ./$DST_NAME.tar -r $1
