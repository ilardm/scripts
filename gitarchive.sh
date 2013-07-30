#!/bin/bash

if [[ ! $1 ]]; then
    echo "no revision specified";
    exit 1;
fi;

DST_NAME="$(pwd | sed 's/.*\///')_$1";
git archive --format=tar --prefix="$DST_NAME/" -o ../"$DST_NAME.tar" "$1"
