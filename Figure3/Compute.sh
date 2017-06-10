#!/bin/bash

# Compute.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Compute data for Figure 3.
#   Enqueues 49 networks.

# Command Line Arguments:
#   Argument 1 (optional): job submission command (e.g. qsub). Can be left blank.

mkdir -p computations

for i in 0{0..9} {10..48}; do
  python ../Query/Enqueue.py computations networks/network${i} S EE Rp $1
done
