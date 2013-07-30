#!/bin/bash

if [ ! $1 ]; then
    echo "no video";
    exit 1;
fi;

VIN=$1;
VOUT="$VIN.mp4";
VRES="/tmp/vid";

mplayer -endpos 1 "$VIN" | grep VIDEO > $VRES;
NVRES=$(cat $VRES | awk '{split($3, res, "x"); resx=int(int(res[1])/3*2); resx=resx-resx%2; resy=int(int(res[2])/3*2); printf "%dx%d", resx, resy;}');

echo $NVRES;

ffmpeg -y -i "$VIN" -b 700000 -r 24 -s $NVRES -vcodec mpeg4 -ab 128000 -ac 2 -acodec mp2 "$VOUT"
