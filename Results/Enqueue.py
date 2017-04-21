# Enqueue.py
# Shaun Harker
# 2017-04-02
# MIT LICENSE

# Enqueue jobs for Query paper on a cluster

import subprocess
import DSGRN
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
      print("./Enqueue.py network_specification_file.txt")
      exit(1)
    network_specification_file = str(sys.argv[1])
    network = DSGRN.Network(network_specification_file);
    print(network.graphviz())
    parametergraph = DSGRN.ParameterGraph(network)
    S_index = network.index('S')
    N = parametergraph.size()
    M = len(parametergraph.factorgraph(S_index))
    L = N / M  # number of reduced parameter index
    Jmax = 2000 # maximum number of jobs to split into
    Kmin = 1000 # minimum number of reduced parameters per job
    K = max(Kmin, int(L/2000))  # number of reduced parameter indices per job
    jobs = [ 'qsub ./QueryPaperShard.sh ' + network_specification_file + ' ' + str(i) + ' ' + str(min(i+K,L)) for i in range(0, L, K)]
    print(jobs)
    for job in jobs:
        subprocess.call(job, shell=True)
