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
#   Argument 4: gene_name  (name of gene used for factor graph search)

network_folder=$1
computation_folder=$2
results_folder=$3
gene_name=$4 

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

mkdir -p $3

${DIR}/CollateJobs.sh $1 $2 $3 $4 > $3/summary.txt
python ${DIR}/parse_summary.py  $3/summary.txt > $3/summary.json
python ${DIR}/draw_networks.py $1 $3
python ${DIR}/make_table.py $3/summary.json $3/table.csv $3/table.md
