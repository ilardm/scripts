#!/bin/bash
# Description:  Получить охуенный блять совет с http://fucking-great-advice.ru
# File:         get-fuckin-advice.sh
# Author:       zm8 <www.axisful.me/cactus/shell/get-fucking-advice>
# Requirements: lynx
# Version:      1.1

rand_url=$(lynx -source "http://fucking-great-advice.ru" -reload | \
        egrep 'id="another"' | egrep -o 'http:\/\/[^\"]*\b')

# URL of advice
# echo advice URL: $advice

# echo -e "\033[1m$(lynx -source $rand_url | egrep 'id="advice"' | \
#         sed -e 's@<[^>]*>@@gi' -e 's@\s*@ @' -e 's@&nbsp;@ @g' -e 's@^\s*@@' | \
#         iconv -f cp1251 -t utf8)\033[0m"
echo -e "$(lynx -source $rand_url | egrep 'id="advice"' | \
        sed -e 's@<[^>]*>@@gi' -e 's@\s*@ @' -e 's@&nbsp;@ @g' -e 's@^\s*@@' | \
        iconv -f cp1251 -t utf8 | sed 's/\r//')"
