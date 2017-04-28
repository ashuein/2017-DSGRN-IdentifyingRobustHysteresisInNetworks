# 2017-DSGRN-GeneNetworksToDynamicPhenotypes

## Overview 

This code repository is supplemental to the paper "From gene networks to their dynamic phenotypes" by Bree Cummins, Tomas Gedeon, Shaun Harker, and Konstantin Mischaikow. It provides instructions for reproducing the computational results presented therein.

## Installation


## Instructions

The computations are quite lengthly and with hardware available in 2017 require approximately 4 months to complete on a single CPU. On the other hand they can be done in parallel on a cluster (which is the setting in which the results were computed)

```bash
enqueue_all.sh YaoNetworks
# Wait until all jobs are complete.
```

Once all jobs are complete:

```bash
collate_all.sh YaoNetworks > small_summary.txt
python parse_collate.py small_summary.txt > small_summary.json
python make_table.py small_summary.json
```

### Figure 5

```bash
enqueue_all.sh networks
# Wait until all jobs are complete.
```

Once all jobs are complete:

```bash
collate_all.sh networks > summary.txt
python parse_collate.py summary.txt > summary.json
python make_table.py summary.json
```

