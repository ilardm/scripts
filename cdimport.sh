#!/bin/bash

# original source http://habrahabr.ru/post/97316/
# apt-get install cdparanoia cdrda cuetools flac lame

rm -f CDImage.wav disk.cue disk.toc *.wav *.flac *.mp3

COVER="cover.jpg";

if [ $1 ] && [ -f "$1" ];
then
    COVER=$1;
fi;

cdparanoia -vzl -O +48 [::]- CDImage.wav
cdrdao read-toc disk.toc
cueconvert -i toc disk.toc disk.cue
cuebreakpoints disk.cue | shnsplit -o wav CDImage.wav

flac --picture="$COVER" --replay-gain -8 split-track*.wav

for i in split-track*.wav; do
    lame -m j --replaygain-accurate -v -b 192 -B 320 --ti "$COVER" "$i" "${i%.wav}.mp3";
done;
