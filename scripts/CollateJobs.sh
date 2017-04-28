#!/bin/bash

for file in `ls -I '*.*' $1`; do

  echo "Network:"
  echo $file

  echo "Number of reduced parameter indices = "
  python NumReducedParameterIndex.py $1/$file

  ./collate.sh $1/computations/$file

  echo "Number of hysteresis matches = "
  echo `wc -w "$1/computations/${file}_hysteresis.txt"`

  echo "Number of resettable bistability matches = "
  echo `wc -w "$1/computations/${file}_resettable.txt"`

  echo " "
done

