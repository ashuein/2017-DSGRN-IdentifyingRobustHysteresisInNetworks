#!/bin/bash

# Compute.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Compute data for Figure 3.
#   Enqueues 49 networks.

# Command Line Arguments:
#   Argument 1 (optional): job submission command (e.g. qsub). Can be left blank.

ENQUEUE=../Query/Enqueue.py
NETWORKS=../Networks

mkdir -p computations


mkdir -p computations/CycD_E2F
for netspec in `ls ${NETWORKS}/CycD_E2F`; do
  python $ENQUEUE computations/CycD_E2F ${NETWORKS}/CycD_E2F/${netspec} CycD E2F $1
done

mkdir -p computations/Myc_E2F
for netspec in `ls ${NETWORKS}/Myc_E2F`; do
  python $ENQUEUE computations/Myc_E2F ${NETWORKS}/Myc_E2F/${netspec} Myc E2F $1
done

mkdir -p computations/Rb_E2F
for netspec in `ls ${NETWORKS}/Rb_E2F`; do
  python $ENQUEUE computations/Rb_E2F ${NETWORKS}/Rb_E2F/${netspec} Rb E2F $1
done

mkdir -p computations/EE_EE
for netspec in `ls ${NETWORKS}/EE_EE`; do
  python $ENQUEUE computations/EE_EE ${NETWORKS}/EE_EE/${netspec} EE EE $1
done

mkdir -p computations/MD_EE
for netspec in `ls ${NETWORKS}/MD_EE`; do
  python $ENQUEUE computations/MD_EE ${NETWORKS}/MD_EE/${netspec} MD EE $1
done

mkdir -p computations/Rp_EE
for netspec in `ls ${NETWORKS}/Rp_EE`; do
  python $ENQUEUE computations/Rp_EE ${NETWORKS}/Rp_EE/${netspec} Rp EE $1
done

mkdir -p computations/SBF_Whi5_SBF
for netspec in `ls ${NETWORKS}/SBF_Whi5_SBF`; do
  python $ENQUEUE computations/SBF_Whi5_SBF ${NETWORKS}/SBF_Whi5_SBF/${netspec} SBF_Whi5 SBF $1
done
