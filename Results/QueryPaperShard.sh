#!/bin/bash
#Active comments for SGE
#$ -V
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe orte 1

# $1 network_specification_file.txt
# $2 starting_rpi
# $3 ending_rpi

python ComputeQuery.py $1 $1_hysteresis_$2_$3.txt $1_resettable_$2_$3.txt $2 $3
