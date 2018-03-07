# 2017-DSGRN-IdentifyingRobustHysteresisInNetworks

[![DOI](https://zenodo.org/badge/80869262.svg)](https://zenodo.org/badge/latestdoi/80869262)

Shaun Harker and Bree Cummins

## Overview 

This code repository is supplemental to the paper "Identifying robust hysteresis in networks" by Bree Cummins, Tomas Gedeon, Shaun Harker, and Konstantin Mischaikow. It provides instructions for reproducing the computational results presented therein.

## Installation


## Instructions

(Note: for cluster users, there is a slight change to these instructions, see below.)

### Positive influence on input node

```bash
cd Positive
./Compute.sh
# Wait until jobs are finished.
./Postprocess.sh
```

### Negative influence on input node

```bash
cd Negative
./Compute.sh
# Wait until jobs are finished.
./Postprocess.sh
```

## Notes on HPC Computing Clusters

The computations are quite lengthly and with hardware available in 2017 require approximately 4 months to complete on a single CPU. On the other hand they can be done in parallel on a cluster (which is the setting in which the results were computed). To utilize a cluster it may be necessary to create a submission script. By default an SGE (Sun Grid Engine) script is available (see ./Query/Shard.sh). To utilize it, instead of typing `./Compute.sh` in the above instruction, type

```bash
./Compute.sh qsub
```

which instructs the code to use the `qsub` command to submit jobs to the cluster queue. If there is a different submission script name, then substitute the appropriate command for qsub, and tweak the submission script `./Query/Shard.sh` as necessary.

