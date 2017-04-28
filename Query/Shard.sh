#!/bin/bash
#Active comments for SGE
#$ -V
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe orte 1

# $1 output_folder
# $2 network_specification_file
# $3 starting_rpi
# $4 ending_rpi
# $5 gene (name) on which to do factor graph query
# $6 gene (name) which is on when in proliferative FP and off in quiescent FP
# $7 gene (name) which is on when in quiescent FP and off in proliferative FP

A=$1
B=`basename $2`
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python ${DIR}/ComputeQuery.py $2 ${A}/${B}_hysteresis_$3_$4.txt ${A}/${B}_resettable_$3_$4.txt $3 $4 $5 $6 $7
