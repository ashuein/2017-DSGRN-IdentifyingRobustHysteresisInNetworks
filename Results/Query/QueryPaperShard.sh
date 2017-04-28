#!/bin/bash
#Active comments for SGE
#$ -V
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe orte 1

# $1 network_specification_file
# $2 starting_rpi
# $3 ending_rpi
# $4 gene (name) on which to do factor graph query
# $5 gene (name) which is on when in proliferative FP and off in quiescent FP
# $6 gene (name) which is on when in quiescent FP and off in proliferative FP

A:=`dirname $1`
B:=`basename $1`
mkdir -p ${A}/computations
python ComputeQuery.py $1 ${A}/computations/${B}_hysteresis_$2_$3.txt ${A}/computations/${B}_resettable_$2_$3.txt $2 $3 $4 $5 $6
