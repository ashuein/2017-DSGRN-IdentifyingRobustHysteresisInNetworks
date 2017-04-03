#!/bin/bash
#Active comments for SGE
#$ -V
#$ -cwd
#$ -j y
#$ -S /bin/bash
#$ -pe orte 1

python ComputeQuery.py hysteresis_out_$1_$2.txt resettable_out_$1_$2.txt $1 $2
