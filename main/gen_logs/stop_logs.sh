#!/bin/bash

export pid=`ps -ef | grep 'python.*[ ]lib/reviewgenarator.py' | awk 'NR==1{print $2}' | cut -d' ' -f1`;kill $pid

exit 0
