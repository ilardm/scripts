#!/bin/bash

if ( test -d /media/WDext4/ilya/backups/netbook/ );
then 
#echo "will backup"
python ~/exe/backuper.py > ~/.backuper/logs/$(date +%Y%m%d-%H%M%S).log
else
echo "can't find external drive plugged in. exit" > ~/.backuper/logs/$(date +%Y%m%d-%H%M%S).log
fi;
