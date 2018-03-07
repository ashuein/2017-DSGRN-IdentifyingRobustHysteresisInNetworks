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
#   Argument 5: output gene name for query

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for file in `ls $1`; do

  echo "Network:"
  echo $file

  echo "Input Node:"
  echo $4

  echo "Output Node:"
  echo $5

  echo "Number of reduced parameter indices = "
  python ${DIR}/NumReducedParameterIndex.py $1/$file $4

  ${DIR}/collate.sh $file $2 $3

  echo "Time to compute partial path hysteresis query (in seconds):"
  cat $3/${file}_partial_hysteresis.time

  echo "Number of partial path hysteresis matches = "
  cat $3/${file}_partial_hysteresis.result
  #echo `wc -w "$3/${file}_hysteresis.txt"`

  echo "Time to compute partial path resettable bistability query (in seconds):"
  cat $3/${file}_partial_resettable.time

  echo "Number of partial path resettable bistability matches = "
  cat $3/${file}_partial_resettable.result
  #echo `wc -w "$3/${file}_resettable.txt"`

  echo "Time to compute full path hysteresis query (in seconds):"
  cat $3/${file}_full_hysteresis.time

  echo "Number of full path hysteresis matches = "
  cat $3/${file}_full_hysteresis.result
  #echo `wc -w "$3/${file}_hysteresis.txt"`

  echo "Time to compute full path resettable bistability query (in seconds):"
  cat $3/${file}_full_resettable.time

  echo "Number of full path resettable bistability matches = "
  cat $3/${file}_full_resettable.result
  #echo `wc -w "$3/${file}_resettable.txt"`


  echo " "
done

