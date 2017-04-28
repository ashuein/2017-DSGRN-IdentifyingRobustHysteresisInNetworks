#!/bin/bash

# Compute.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Compute data for Figure 5

# Command Line Arguments:
#   Argument 1 (optional): job submission command (e.g. qsub). Can be left blank.

python ../Query/Enqueue.py networks/network_7 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_2a7 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_2b7 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_2a2b7 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_8 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_2a8 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_2b8 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_2a2b8 S E2F E2F_Rb $1
python ../Query/Enqueue.py networks/network_yeaststart S SBF SBF_Whi5 $1
