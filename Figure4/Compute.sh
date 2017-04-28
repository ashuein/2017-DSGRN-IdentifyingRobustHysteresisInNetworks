#!/bin/bash
# optional parameter: leave blank for sequential operation
#                      on cluster, give job submission command (e.g. qsub)

## Enqueue 49 networks for Figure 4 computations.

for i in 0{0..9} {10..48}; do
  python Query/Enqueue.py YaoNetworks/network${i}.txt S EE Rp $1
done
