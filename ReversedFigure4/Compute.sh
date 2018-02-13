#!/bin/bash

# Compute.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Compute data for Figure 4

# Command Line Arguments:
#   Argument 1 (optional): job submission command (e.g. qsub). Can be left blank.

mkdir -p computations

python ../Query/ReverseEnqueue.py computations networks/network_yeaststart SBF_Whi5 SBF $1
