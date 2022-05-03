#!/bin/bash

rm -rf temp.log

if ! command -v sensors &> /dev/null; then
    sudo apt-get install lm-sensors
    sudo sensors-detect
fi

while true; do
    { date; printf "\n"; sensors; printf "----------- \n"; } >> temp.log
    sleep 1
done
