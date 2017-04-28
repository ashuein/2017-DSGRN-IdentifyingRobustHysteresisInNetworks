#!/bin/bash

# collate.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Given a network and the location of the "shard" files computed,
#   collate them together (via concatenation) 
#   For the time logs, concatenate the logs, and then sum them.

# Command Line Arguments:
#   argument 1: network name
#   argument 2: location of shard files
#   argument 3: location to store collated files

rm -f $3/$1_hysteresis.txt
rm -f $3/$1_hysteresis.log

rm -f $3/$1_resettable.txt
rm -f $3/$1_resettable.log

cat $2/$1_hysteresis*.txt > $3/$1_hysteresis.txt
cat $2/$1_hysteresis*.log > $3/$1_hysteresis.log

cat $2/$1_resettable*.txt > $3/$1_resettable.txt
cat $2/$1_resettable*.log > $3/$1_resettable.log

echo "Time to compute hysteresis query (in seconds):"
awk '{ sum += $1 } END { print sum }' $3/$1_hysteresis.log > $3/$1_hysteresis.log

echo "Time to compute resettable bistability query (in seconds):"
awk '{ sum += $1 } END { print sum }' $3/$1_resettable.log > $3/$1_resettable.log
