#!/bin/bash

IP="192.168.1.X";
DIR="dir"

case $1 in
	n)
		rsync -aurlvhn --exclude=push.sh --exclude=lastsync --delete . ilya@$IP:/home/ilya/$DIR;
		exit;
		;;
	s)
		rsync -aurlvh --exclude=push.sh --exclude=lastsync --delete . ilya@$IP:/home/ilya/$DIR;
		date > lastsync;
		;;
	*)
		echo "use 'n' to dry run";
		echo "use 's' to sync";
		;;
esac;
