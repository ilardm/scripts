#!/bin/bash

# hg glog --color=none . | grep -e "^[o@]" | sed -e 's/.*://' > revisions.txt

if [ ! "$1" ];
then
    echo "specify repository working directory!";
    exit 1;
fi;

TWD="$1";
CWD=$(pwd);

tac "revisions.txt" | while read rev;
do
    echo "processing '$rev'";

    cd "$TWD";

    LOG=$(hg log -yr "$rev");
    AUTHOR=$(echo "$LOG" | grep -P "user:\ *" | sed -e 's/user:\ *//');
    DATE=$(echo "$LOG" | grep -P "date:\ *" | sed -e 's/date:\ *//');
    MSG=$(echo "$LOG" | grep -P "summary:\ *" | sed -e 's/summary:\ *//');

    es=$(hg up -C "$rev");
    es=$(git add .);
    es=$(git commit -am "$MSG" --date="$DATE");

    if [ 0 != $? ];
    then
        echo "oops";
    fi;

    cd "$CWD";
done;
