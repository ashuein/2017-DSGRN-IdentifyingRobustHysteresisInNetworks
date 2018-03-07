#!/bin/bash
# Postprocess.sh
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Calls postprocess script for Figure 3.

../scripts/Postprocess.sh ./networks/CycD_E2F ./computations/CycD_E2F ./results CycD E2F
../scripts/Postprocess.sh ./networks/Myc_E2F ./computations/Myc_E2F ./results Myc E2F
../scripts/Postprocess.sh ./networks/Rb_E2F ./computations/Rb_E2F ./results Rb E2F
../scripts/Postprocess.sh ./networks/MD_EE ./computations/MD_EE ./results MD EE
../scripts/Postprocess.sh ./networks/EE_EE ./computations/EE_EE ./results EE EE
../scripts/Postprocess.sh ./networks/Rb_EE ./computations/Rb_EE ./results Rb EE
../scripts/Postprocess.sh ./networks/SBF_Whi5_SBF ./computations/SBF_Whi5_SBF ./results SBF_Whi5 SBF

