#!/bin/bash

## Enqueue 49 networks for Figure 4 computations.

for i in 0{0..9} {10..48}; do
  python Query/Enqueue.py YaoNetworks/network${i}.txt S EE Rp $1
done
