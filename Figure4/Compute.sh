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

# python ../Query/Enqueue.py computations networks/network_7 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_2a7 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_2b7 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_2a2b7 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_8 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_2a8 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_2b8 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_2a2b8 S E2F Rb $1
python ../Query/Enqueue.py computations networks/network_neither7nor8 S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_7p27 S E2F Rb $1
python ../Query/Enqueue.py computations networks/network_2a S E2F Rb $1
python ../Query/Enqueue.py computations networks/network_2b S E2F Rb $1
python ../Query/Enqueue.py computations networks/network_2a2b S E2F Rb $1
# python ../Query/Enqueue.py computations networks/network_yeaststart S SBF SBF_Whi5 $1
