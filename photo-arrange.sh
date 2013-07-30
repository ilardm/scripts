#!/bin/bash

for i in *.jpg *.JPG; do
    # echo "process file $i";

    # get datetime
    DST=$(identify -format %[exif:DateTimeOriginal] "$i");

    # check if not blank and try another
    if [ -z "$DST" ]; then
        DST=$(identify -format %[exif:DateTimeDigitized] "$i");
    fi;

    # leave just file name if no EXIF info in file
    if [ -z "$DST" ]; then
        DST="${i%.*}";
    fi;

    DST="$DST.jpg";

    echo "$i -> $DST";

    mv -i "$i" "$DST.jpg";
done;

