#!/bin/bash

# CollateJobs.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Loop through network files and collate computational results.
#   Output a summary to standard output

# Command line arguments:
#   Argument 1: folder containing network files
#   Argument 2: folder containing computational results
#   Argument 3: folder to store collated results in

for file in `ls -I '*.*' $1`; do

  echo "Network:"
  echo $file

  echo "Number of reduced parameter indices = "
  python NumReducedParameterIndex.py $1/$file

  ./collate.sh $file $2 $3

  echo "Time to compute hysteresis query (in seconds):"
  cat $3/${file}_hysteresis.log

  echo "Time to compute resettable bistability query (in seconds):"
  cat $3/${file}_resettable.log

  echo "Number of hysteresis matches = "
  echo `wc -w "$3/${file}_hysteresis.txt"`

  echo "Number of resettable bistability matches = "
  echo `wc -w "$3/${file}_resettable.txt"`

  echo " "
done

