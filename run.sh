#!/bin/bash

here=`dirname $0`
cd $here

result=`python3 ./main.py 2>&1 > /dev/tty`
if [ $? -eq 0 ]; then
	echo $result
else
	exit 1
fi