#!/bin/bash

echo "enter root password to call grps"
sudo rfcomm bind /dev/rfcomm0 00:12:62:A9:1F:90 3
sudo wvdial n6680
