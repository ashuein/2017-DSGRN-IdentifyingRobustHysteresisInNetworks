#!/bin/bash

# Compute.sh
# Shaun Harker
# 2018-02-13
# MIT LICENSE

# Command Line Arguments:
#   Argument 1 (optional): job submission command (e.g. qsub). Can be left blank.

mkdir -p computations
mkdir -p networks
python GenerateThreeNode.py
mv networks bignetworks
mkdir -p networks
for file in `ls bignetworks | grep "0"`; do
  mv ./bignetworks/$file networks
done

for filename in `ls networks`; do
  python ../Query/SingleJobEnqueue.py computations networks/${filename} X0 X2 $1
done
