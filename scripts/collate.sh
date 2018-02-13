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

rm -f $3/$1_partial_hysteresis.txt
rm -f $3/$1_partial_hysteresis.log

rm -f $3/$1_partial_resettable.txt
rm -f $3/$1_partial_resettable.log

rm -f $3/$1_full_hysteresis.txt
rm -f $3/$1_full_hysteresis.log

rm -f $3/$1_full_resettable.txt
rm -f $3/$1_full_resettable.log

cat $2/$1_partial_hysteresis*.txt > $3/$1_partial_hysteresis.txt
cat $2/$1_partial_hysteresis*.log > $3/$1_partial_hysteresis.log

cat $2/$1_partial_resettable*.txt > $3/$1_partial_resettable.txt
cat $2/$1_partial_resettable*.log > $3/$1_partial_resettable.log

cat $2/$1_full_hysteresis*.txt > $3/$1_full_hysteresis.txt
cat $2/$1_full_hysteresis*.log > $3/$1_full_hysteresis.log

cat $2/$1_full_resettable*.txt > $3/$1_full_resettable.txt
cat $2/$1_full_resettable*.log > $3/$1_full_resettable.log

#echo "Time to compute partial hysteresis query (in seconds):"
awk '{ sum += $1 } END { print sum }' $3/$1_partial_hysteresis.log > $3/$1_partial_hysteresis.time

#echo "Time to compute partial resettable bistability query (in seconds):"
awk '{ sum += $1 } END { print sum }' $3/$1_partial_resettable.log > $3/$1_partial_resettable.time

#echo "Time to compute full hysteresis query (in seconds):"
awk '{ sum += $1 } END { print sum }' $3/$1_full_hysteresis.log > $3/$1_full_hysteresis.time

#echo "Time to compute full resettable bistability query (in seconds):"
awk '{ sum += $1 } END { print sum }' $3/$1_full_resettable.log > $3/$1_full_resettable.time

awk '{ sum += $1; total += $2 } END { print sum " " total }' $3/$1_partial_hysteresis.txt > $3/$1_partial_hysteresis.result
awk '{ sum += $1; total += $2 } END { print sum " " total }' $3/$1_partial_resettable.txt > $3/$1_partial_resettable.result

awk '{ sum += $1; total += $2 } END { print sum " " total }' $3/$1_full_hysteresis.txt > $3/$1_full_hysteresis.result
awk '{ sum += $1; total += $2 } END { print sum " " total }' $3/$1_full_resettable.txt > $3/$1_full_resettable.result

