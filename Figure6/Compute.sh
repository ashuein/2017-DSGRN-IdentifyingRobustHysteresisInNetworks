#!/bin/bash
# Compute.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Compute data for Figure 6

# Command Line Arguments:
#   Argument 1 (optional): job submission command (e.g. qsub). Can be left blank.

mkdir -p computations

python ../Query/Enqueue.py computations networks/network_7p27 S E2F E2F_Rb $1
