#!/bin/bash
#Active comments for SGE
#$ -V
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe orte 1

# $1 Python script to run
# $2 output_folder
# $3 network_specification_file
# $4 starting_rpi
# $5 ending_rpi
# $6 gene (name) on which to do factor graph query
# $7 gene (name) which is on when in proliferative FP and off in quiescent FP

A=$2
B=`basename $3`
python $1 $3 ${A}/${B}_hysteresis_$4_$5.txt ${A}/${B}_resettable_$4_$5.txt $4 $5 $6 $7
