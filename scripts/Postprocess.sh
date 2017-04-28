#!/bin/bash

# Postprocess.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Collate the results of computation, and create summary files.

# Command Line Arguments:
#   Argument 1: network_folder  (folder containing networks for which computations have been done)
#   Argument 2: computation_folder  (folder to find computational shard files in)
#   Argument 3: results_folder  (folder to store collated results in)

network_folder=$1
computation_folder=$2
results_folder=$3

./scripts/CollateJobs.sh $1 $2 $3 > $3/summary.txt
python ./scripts/parse_summary.py  $3/summary.txt > $3/summary.json
python ./scripts/make_table.py $3/summary.json $3/table.md
