# 2017-DSGRN-QueryExperiments

## Installation

### Dependencies

* Python
* DSGRN

## Experiment 0

### Overview

```
X1 : (X1)(X2+~X3)
X2 : X1 
X3 : (X1)(~X2)
```

### Procedure

First produce the database.

```bash
DSGRN_PATH=/path/to/DSGRN
cd Experiments
time mpiexec -np 8 $DSGRN_PATH/software/Signatures/bin/Signatures 00_Experiment.txt 00_Experiment.db
```

Next we run the query experiments.

```bash
python 01_Experiment.py > 01_Experiment.log
```

### Results

* TODO

## Experiment 1

### Overview

This is timing experiment for the following network with approximately 1.2 billion parameters, given in DSGRN network specification format.

```json
S : S  
Myc : E2F + S : E
CycD : Myc + E2F : E 
CycE : E2F : E
E2F : (Myc + E2F)(~E2F_Rb) : E
E2F_Rb : (E2F)(~CycD)(~CycE) : E
```
A factor graph was created over the variable ```S```, resulting in 212,103,360 reduced parameters. We randomly sampled 10,000 reduced parameters 1000 times in order to estimate the total computational cost of the procedure.

### Procedure

We performed the experiment on a cluster using the SGE scheduler as a single-threaded process with the following:

```bash
qsub ./cluster/sge.sh ./Experiments/01_Experiment.py
```

### Results

* TODO

