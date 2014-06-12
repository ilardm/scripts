#!/bin/bash

if [ ! $1 ]; then
    echo "specify directory";
    exit 1;
fi;

TARGET_DIR=$1;

for i in $(find "$TARGET_DIR" -type f -executable); do
    TARGET=$(echo "$i" | sed 's/.*\///');
    echo "update alternative for '$TARGET'";

    update-alternatives --install "/usr/bin/$TARGET" "$TARGET" "$i" 10000;
    update-alternatives --config "$TARGET";
done;
