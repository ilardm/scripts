#!/bin/bash

if [[ ! $1 && ! $2 ]]; then
	echo "specify: [ on <resolution> <position> [rrate]] [ off ]";
	exit 1
fi

NMODE="--right-of";
RRATE="60";

case $1 in
on)
	if [[ $3 ]]; then
		case $3 in
		up)
			NMODE="--above";
			;;
		down)
			NMODE="--below";
			;;
		left)
			NMODE="--left-of";
			;;
		right)
			NMODE="--right-of";
			;;
		clone)
			NMODE="--same-as";
			;;
		*)
			NMODE="--right-of";
			;;
		esac;
	else
		NMODE="--right-of";
	fi;

	if [[ $4 ]]; then
		RRATE=$4;
	else
		RRATE="60";
	fi;

	xrandr --output LVDS1 --auto --pos 0x0 --output VGA1 --mode $2 -r $RRATE $NMODE LVDS1;
	;;
off)
	xrandr --output LVDS1 --auto --pos 0x0 --output VGA1 --off;
	;;
*)
	echo "unknown option";
	;;
esac;
