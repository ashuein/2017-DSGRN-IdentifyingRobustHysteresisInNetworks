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

network = DSGRN.Network()
network.assign(("S : S\n"
               "Myc : E2F + S : E\n"
               "CycD : Myc + E2F : E\n"
               "CycE : E2F : E\n"
               "E2F : (Myc + E2F)(~E2F_Rb) : E\n"
               "E2F_Rb : (E2F)(~CycD)(~CycE) : E\n"))
E2F_index = network.index('E2F')
E2F_Rb_index = network.index('E2F_Rb')

parametergraph = DSGRN.ParameterGraph(network)

def AnalyzeParameter(parameterindex):
    parameter = parametergraph.parameter(parameterindex)
    dg = DSGRN.DomainGraph(parameter)
    md = DSGRN.MorseDecomposition(dg.digraph())
    mg = DSGRN.MorseGraph()
    mg.assign(dg, md)
    return mg

def is_FP(annotation):
    return annotation.startswith("FP")

def is_quiescent_FP(annotation):
    #FP_OFF={"E2F":[0,0],"E2F_Rb":[1,1]} 
    if is_FP(annotation):
        digits = [int(s) for s in annotation.replace(",", "").split() if s.isdigit()]
        if digits[E2F_index] == 0 and digits[E2F_Rb_index] == 1:
            return True
    return False

def is_proliferative_FP(annotation):
    #FP_ON={"E2F":[1,8],"E2F_Rb":[0,0]}
    if is_FP(annotation):
        digits = [int(s) for s in annotation.replace(",", "").split() if s.isdigit()]
        if digits[E2F_index] >= 1 and digits[E2F_Rb_index] == 0:
            return True
    return False

def AnalyzeMorseGraph(mg):
    mg_poset = mg.poset()
    stable_annotations = [ mg.annotation(i)[0] for i in range(0,mg.poset().size()) if len(mg.poset().children(i)) == 0]
    monostable = len(stable_annotations) == 1
    quiescent = any( is_quiescent_FP(annotation) for annotation in stable_annotations )
    proliferative = any( is_proliferative_FP(annotation) for annotation in stable_annotations )
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
def Classify(parameterindex):
    return AnalyzeMorseGraph(AnalyzeParameter(parameterindex))

class ComputeHysteresisQuery:
    def __init__(self, network, gene):
        self.query = DSGRN.ComputeSingleGeneQuery(network,'S',Classify)
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
    def __init__(self, network, gene):
        self.labeller = lambda pi : (lambda label : 'O' if (label == 'p' or label == 'P' ) else label)(Classify(pi))
        self.query = DSGRN.ComputeSingleGeneQuery(network,'S',self.labeller)
        self.patterngraph = DSGRN.Graph(set([0,1,2]), [(0,0),(1,1),(0,1),(1,0),(0,2),(1,2)])
        self.patterngraph.matching_label = lambda v : { 0:'Q', 1:'q', 2:'B' }[v]
        self.matching_relation = lambda label1, label2 : label1 == label2
        self.memoization_cache = {}
        
    def __call__(self, reduced_parameter_index):
        searchgraph = self.query(reduced_parameter_index)
        searchgraphstring = ''.join([ searchgraph.matching_label(v) for v in searchgraph.vertices ])
        if searchgraphstring not in self.memoization_cache:
            alignment_graph = DSGRN.AlignmentGraph(searchgraph, self.patterngraph, self.matching_relation)
            root_vertex = (0,0)
            def check(n):
                if searchgraph.matching_label(n) != 'B':
                    return False
                leaf_vertex = (n,len(patterngraph.vertices)-1) 
                is_reachable = alignment_graph.reachable(root_vertex, leaf_vertex) 
                return is_reachable
            self.memoization_cache[searchgraphstring] = any( check(n) for n in range(1,len(searchgraph.vertices)))
        return self.memoization_cache[searchgraphstring]

if __name__ == "__main__":
    if len(sys.argv) < 5:
      print("./ComputeQuery hysteresis_output_file.txt resettable_output_file.txt starting_rpi ending_rpi")
      exit(1)
    hysteresis_output_file = str(sys.argv[1])
    resettable_output_file = str(sys.argv[2])
    starting_rpi = int(sys.argv[3])
    ending_rpi = int(sys.argv[4])
    hysteresis_query = ComputeHysteresisQuery(network, 'S')
    resettable_query = ComputeResettableBistabilityQuery(network, 'S')
    hysteresis_query_result = []
    resettable_query_result = []
    for rpi in range(starting_rpi, ending_rpi):
      if hysteresis_query(rpi):
        hysteresis_query_result.append(rpi)
      if resettable_query(rpi):
        resettable_query_result.append(rpi)
      if rpi % 10000 == 0:
        DSGRN.LogToSTDOUT("Processed from " + str(starting_rpi) + " to " + str(rpi))
    with open(hysteresis_output_file, 'w') as outfile:
      outfile.write('\n'.join([str(rpi) for rpi in hysteresis_query_result ]))
    with open(resettable_output_file, 'w') as outfile:
      outfile.write('\n'.join([str(rpi) for rpi in resettable_query_result ]))
    exit(0)
