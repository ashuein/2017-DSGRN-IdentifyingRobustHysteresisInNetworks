# ComputeQuery.py
# Shaun Harker
# 2017-04-02
# MIT LICENSE

# This file is meant to analyze a specific network
# for queries indicated in the "Query" paper

import DSGRN
from memoize import memoize
import time
import sys

class PQNetworkAnalyzer:
    def __init__(self, network, P):
        self.network = network
        self.P_index = network.index(P)
        self.parametergraph = DSGRN.ParameterGraph(network)

    def AnalyzeParameter(self, parameterindex):
        parameter = self.parametergraph.parameter(parameterindex)
        dg = DSGRN.DomainGraph(parameter)
        md = DSGRN.MorseDecomposition(dg.digraph())
        mg = DSGRN.MorseGraph()
        mg.assign(dg, md)
        return mg

    def is_FP(self, annotation):
        return annotation.startswith("FP")

    def is_quiescent_FP(self, annotation):
        if self.is_FP(annotation):
            digits = [int(s) for s in annotation.replace(",", "").split() if s.isdigit()]
            if digits[self.P_index] == 0:
                return True
        return False

    def is_proliferative_FP(self, annotation):
        if self.is_FP(annotation):
            digits = [int(s) for s in annotation.replace(",", "").split() if s.isdigit()]
            if digits[self.P_index] >= 1:
                return True
        return False

    def AnalyzeMorseGraph(self, mg):
        mg_poset = mg.poset()
        stable_annotations = [ mg.annotation(i)[0] for i in range(0,mg.poset().size()) if len(mg.poset().children(i)) == 0]
        monostable = len(stable_annotations) == 1
        quiescent = any( self.is_quiescent_FP(annotation) for annotation in stable_annotations )
        proliferative = any( self.is_proliferative_FP(annotation) for annotation in stable_annotations )
        if monostable and quiescent:
            return 'Q'
        if monostable and proliferative:
            return 'P'
        if quiescent and proliferative:
            return 'B'
        if quiescent:
            return 'q'
        if proliferative:
            return 'p'
        return 'O'

    @memoize
    def Classify(self, parameterindex):
        return self.AnalyzeMorseGraph(self.AnalyzeParameter(parameterindex))

class ComputeHysteresisQuery:
    def __init__(self, network, S, P):
        self.network = network 
        self.analyzer = PQNetworkAnalyzer(self.network, P)
        self.query = DSGRN.ComputeSingleGeneQuery(network,S,self.analyzer.Classify)
        self.patterngraph = DSGRN.Graph(set([0,1,2,3,4]), [(0,0),(1,1),(0,1),(1,0),(0,2),(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(4,3)])
        self.patterngraph.matching_label = lambda v : { 0:'Q', 1:'q', 2:'B', 3:'p', 4:'P' }[v]
        self.matching_relation = lambda label1, label2 : label1 == label2
        self.memoization_cache = {}


    def __call__(self,reduced_parameter_index):
        searchgraph = self.query(reduced_parameter_index)
        searchgraphstring = ''.join([ searchgraph.matching_label(v) for v in searchgraph.vertices ])
        if searchgraphstring not in self.memoization_cache:
            alignment_graph = DSGRN.AlignmentGraph(searchgraph, self.patterngraph, self.matching_relation)
            root_vertex = (0,0)
            leaf_vertex = (len(searchgraph.vertices)-1, 4)
            is_reachable = alignment_graph.reachable(root_vertex, leaf_vertex) 
            self.memoization_cache[searchgraphstring] = is_reachable
        return self.memoization_cache[searchgraphstring]

class ComputeResettableBistabilityQuery:
    def __init__(self, network, S, P):
        self.network = network 
        self.analyzer = PQNetworkAnalyzer(self.network, P)
        # label P, p, and O as disallowed "d"
        # label Q, q as allowed "a"
        # label B as terminal "t"
        label_map = { 'P':'d', 'p':'d', 'O':'d', 'Q':'a', 'q':'a', 'B': 't'}
        self.labeller = lambda pi : label_map[self.analyzer.Classify(pi)]
        self.query = DSGRN.ComputeSingleGeneQuery(network,S,self.labeller)
        self.memoization_cache = {}
        
    def __call__(self, reduced_parameter_index):
        """
        Graph search for factor graph correspond to reduced_parameter_index.
        Start at Q (at root of factor graph)
        Pass through only q and Q until reach B.
        """
        root_pi = self.query.full_parameter_index(reduced_parameter_index,0,self.query.gene_index)
        if self.analyzer.Classify(root_pi) != 'Q':
            return False
        searchgraph = self.query(reduced_parameter_index)
        searchgraphstring = ''.join([ searchgraph.matching_label(v) for v in searchgraph.vertices ])
        if searchgraphstring not in self.memoization_cache:
            allowed = lambda v : searchgraph.matching_label(v) == 'a'
            terminal = lambda v : searchgraph.matching_label(v) == 't'
            self.memoization_cache[searchgraphstring] = searchgraph.predicate_reachable(0, allowed, terminal) 
        return self.memoization_cache[searchgraphstring]

if __name__ == "__main__":
    if len(sys.argv) < 8:
      print("./ComputeQuery network_specification_file.txt hysteresis_output_file.txt resettable_output_file.txt starting_rpi ending_rpi S_gene P_gene")
      exit(1)
    network_specification_file = str(sys.argv[1])
    hysteresis_output_file = str(sys.argv[2])
    resettable_output_file = str(sys.argv[3])
    starting_rpi = int(sys.argv[4])
    ending_rpi = int(sys.argv[5])
    S = sys.argv[6]
    P = sys.argv[7]

    network = DSGRN.Network(network_specification_file)
    # Hysteresis Query
    start_time = time.time()
    hysteresis_query = ComputeHysteresisQuery(network, S, P)
    hysteresis_query_result = []
    for rpi in range(starting_rpi, ending_rpi):
      if hysteresis_query(rpi):
        hysteresis_query_result.append(rpi)
      if (rpi - starting_rpi) % 10000 == 0:
        DSGRN.LogToSTDOUT("Processed from " + str(starting_rpi) + " to " + str(rpi) + " out of " + str(ending_rpi))
    with open(hysteresis_output_file, 'w') as outfile:
      outfile.write('\n'.join([str(rpi) for rpi in hysteresis_query_result ]) + '\n' )
    with open(hysteresis_output_file + ".log", 'w') as outfile:
      outfile.write(str(time.time() - start_time) + '\n')

    # Resettable Bistability Query
    start_time = time.time()
    resettable_query = ComputeResettableBistabilityQuery(network, S, P)
    resettable_query_result = []
    for rpi in range(starting_rpi, ending_rpi):
      if resettable_query(rpi):
        resettable_query_result.append(rpi)
      if (rpi - starting_rpi) % 10000 == 0:
        DSGRN.LogToSTDOUT("Processed from " + str(starting_rpi) + " to " + str(rpi) + " out of " + str(ending_rpi))
    with open(resettable_output_file, 'w') as outfile:
      outfile.write('\n'.join([str(rpi) for rpi in resettable_query_result ])+ '\n')
    with open(resettable_output_file + ".log", 'w') as outfile:
      outfile.write(str(time.time() - start_time) + '\n')

    exit(0)
