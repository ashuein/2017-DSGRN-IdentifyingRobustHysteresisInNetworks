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

python ../Query/ReverseEnqueue.py computations networks/network_7 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2a7 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2b7 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2a2b7 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_8 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2a8 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2b8 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2a2b8 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_neither7nor8 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_7p27 Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2a Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2b Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_2a2b Myc E2F $1
python ../Query/ReverseEnqueue.py computations networks/network_yeaststart Myc SBF $1
