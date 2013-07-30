#!/bin/bash

XRES=2049
YRES=1025
WND=("Hann" "Hamming" "Bartlett" "Rectangular" "Kaiser")
OPT=("_" "-s" "-m" "-h" "-hm")

if [ ! $1 ];
then
    echo "specify input file";
    exit 1;
fi;

for o in ${OPT[@]}; do
    if [ $o == "_" ]; then
        o="";
    fi;

    for w in ${WND[@]}; do
        CMD="sox $1 -n spectrogram $o -w $w -x $XRES -y $YRES -o s$o-$w-$1.png";
        echo "cmd: \"$CMD\"";
        $CMD;
    done;
done;

