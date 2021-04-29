#!/bin/bash

cd /opt/gen_logs
lib/reviewgenarator.py > logs/access.log &
exit 0
