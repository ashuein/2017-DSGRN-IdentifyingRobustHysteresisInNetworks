#!/bin/bash

# optional parameter: leave blank for sequential operation
#                      on cluster, give job submission command (e.g. qsub)

# Start jobs for Figure 5
python Query/Enqueue.py networks/network_7 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_2a7 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_2b7 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_2a2b7 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_8 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_2a8 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_2b8 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_2a2b8 S E2F E2F_Rb $1
python Query/Enqueue.py networks/network_yeaststart S SBF SBF_Whi5 $1
