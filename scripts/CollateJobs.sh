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
#   Argument 4: gene name for query

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for file in `ls $1`; do

  echo "Network:"
  echo $file

  echo "Number of reduced parameter indices = "
  python ${DIR}/NumReducedParameterIndex.py $1/$file $4

  ${DIR}/collate.sh $file $2 $3

  echo "Time to compute hysteresis query (in seconds):"
  cat $3/${file}_hysteresis.time

  echo "Time to compute resettable bistability query (in seconds):"
  cat $3/${file}_resettable.time

  echo "Number of hysteresis matches = "
  echo `wc -w "$3/${file}_hysteresis.txt"`

  echo "Number of resettable bistability matches = "
  echo `wc -w "$3/${file}_resettable.txt"`

  echo " "
done

