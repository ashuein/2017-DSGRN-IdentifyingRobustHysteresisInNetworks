# NumReducedParameterIndex.py
# Shaun Harker
# 2017-04-18
# MIT LICENSE


import subprocess
import DSGRN
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
      print("./NumReducedParameterIndex.py network_specification_file.txt S_gene")
      exit(1)
    network_specification_file = str(sys.argv[1])
    S = str(sys.argv[2])
    network = DSGRN.Network(network_specification_file);
    parametergraph = DSGRN.ParameterGraph(network)
    S_index = network.index(S)
    N = parametergraph.size()
    M = len(parametergraph.factorgraph(S_index))
    L = N / M  # number of reduced parameter index
    print(L)
