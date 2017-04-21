#!/bin/bash

rm $1_hysteresis.txt
rm $1_hysteresis.log

rm $1_resettable.txt
rm $1_resettable.log

cat $1_hysteresis*.txt > $1_hysteresis.txt
cat $1_hysteresis*.log > $1_hysteresis.log

cat $1_resettable*.txt > $1_resettable.txt
cat $1_resettable*.log > $1_resettable.log

echo "Time to compute hysteresis query (in seconds):"
awk '{ sum += $1 } END { print sum }' $1_hysteresis.log

echo "Time to compute resettable bistability query (in seconds):"
awk '{ sum += $1 } END { print sum }' $1_resettable.log
