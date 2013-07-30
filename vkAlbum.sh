#!/bin/bash

EMAIL=ilardm@gmail.com
PASSWORD=13792580

URL=$( echo $1 | sed 's#http://vkontakte\.ru/album\([0-9]*\)_\([0-9]*\).*#http://vkontakte.ru/photos.php?act=a_album\&oid=\1\&aid=\2#g' )

wget -q --save-cookies=/tmp/vkcookie.txt -O /dev/null "http://vkontakte.ru/login.php?email=$EMAIL&pass=$PASSWORD"

wget -q --load-cookies=/tmp/vkcookie.txt -O- $URL | sed "s/,/\\
/g" | sed -n 's#\"http:\\/\\/cs\([0-9]*\)\.vkontakte\.ru\\/\(u[0-9]*\)\\/\([0-9]*\)\\/\([a-z]_[0-9a-z]*\.jpg\)\"\].*#http://cs\1.vkontakte.ru/\2/\3/\4#gp' | wget -i- -nc

rm /tmp/vkcookie.txt
