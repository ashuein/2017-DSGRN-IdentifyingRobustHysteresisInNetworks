#!/bin/bash
# Postprocess.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

NETWORKS=../Networks

../scripts/Postprocess.sh ${NETWORKS}/CycD_E2F ./computations/CycD_E2F ./results/CycD_E2F CycD E2F
../scripts/Postprocess.sh ${NETWORKS}/Myc_E2F ./computations/Myc_E2F ./results/Myc_E2F Myc E2F
../scripts/Postprocess.sh ${NETWORKS}/Rb_E2F ./computations/Rb_E2F ./results/Rb_E2F Rb E2F
../scripts/Postprocess.sh ${NETWORKS}/MD_EE ./computations/MD_EE ./results/MD_EE MD EE
../scripts/Postprocess.sh ${NETWORKS}/EE_EE ./computations/EE_EE ./results/EE_EE EE EE
../scripts/Postprocess.sh ${NETWORKS}/Rp_EE ./computations/Rp_EE ./results/Rp_EE Rp EE
../scripts/Postprocess.sh ${NETWORKS}/SBF_Whi5_SBF ./computations/SBF_Whi5_SBF ./results/SBF_Whi5_SBF SBF_Whi5 SBF
