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

for filename in `ls networks`; do
  python ../Query/Enqueue.py computations networks/${filename} X0 X2 $1
done
