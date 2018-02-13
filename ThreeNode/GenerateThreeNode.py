# Generate Three Node Networks

import itertools

three = [-1, 0, 1]
somelists = [three, three, three]

input_combinations = [ element for element in itertools.product(*somelists) ]
threelists = [input_combinations, input_combinations, input_combinations]
possibilities = [ element for element in itertools.product(*threelists) ]

# print(possibilities)

# print(len(possibilities))

# goal. remove symmetries   (OOPS -- symmetries didn't matter since input and output node meaningful and breaks symmetry)
#       remove disconnected

# strategy: find heuristics. 

# associate symbol to each node. 
#   self-edge  0, 1, or -1
#   other two in-edges:  1,1 1,0 1,-1 0,0 0,-1, -1,-1
#  6 * 3 = 18 node types. Arbitrarily order them. 

# for a network, determine node types, then sort them, then list of sorted node types is heuristic. 

def NodeSymbol(triple, i):
  # triple is 3-tuple, e.g. (-1, 0, 1)
  # triple[i] is self edge
  if i == 0:
    j = 1
    k = 2
  if i == 1:
    j = 0
    k = 2
  if i == 2:
    j = 0
    k = 1
  # i is self edge, j and k are other edges
  return (triple[i], min(triple[j], triple[k]), max(triple[j], triple[k]))


def NetworkHeuristic(network):
  # "network" is triple of triples, e.g. ((1, 1, 1), (1, 1, 1), (1, 1, -1))
  return tuple(sorted([NodeSymbol(network[i], i) for i in range(0,3)]))

table = {}

def CheckNetworkIsomorphism(network1, network2):
  for pi in itertools.permutations([0, 1, 2]):
    if all( [ network1[i][j] == network2[pi[i]][pi[j]] for i in range(0,3) for j in range(0,3) ]):
      return True 
  return False

def CheckIfNetworkNontrivial(network):
  # if some node has zero inputs, network is trivial
  ab = network[0][1] or network[1][0]
  bc = network[0][2] or network[2][0]
  ac = network[1][2] or network[2][1]
  nonzerooutputs = all(any([ network[j][i] != 0 for j in range(0,3) ]) for i in range(0,3))
  return nonzerooutputs and ( (ab and bc) or (ab and ac) or (bc and ac))

def NetworkFileString(network):
  symbol = { -1 : "R", 0 : "0", 1 : "A" }
  return ''.join([symbol[network[i][j]] for i in range(0,3) for j in range(0,3) ])

def NetworkSpecFile(network):
  spec = ''
  for i in range(0,3):
    spec += 'X' + str(i) + ' : '
    activators = '+'.join([ 'X' + str(j) for j in range(0,3) if network[i][j] == 1])
    repressors = ')('.join([ '~X' + str(j) for j in range(0,3) if network[i][j] == -1])
    if activators:
      activators = '(' + activators + ')'
    if repressors:
      repressors = '(' + repressors + ')'
    spec += activators + repressors + "\n"
  return spec

for network in possibilities:
  if not CheckIfNetworkNontrivial(network):
    continue
  heuristic = NetworkHeuristic(network)
  if heuristic not in table:
    table[heuristic] = []
  # didn't need to check symmetry because input and output node break symmetry
  # if not any( CheckNetworkIsomorphism(network, tabled_network) for tabled_network in table[heuristic]):
  #   table[heuristic].append(network)
  table[heuristic].append(network)

number_of_networks = sum([ len(table[key]) for key in table ])

print(number_of_networks)

for key in table:
  for network in table[key]:
    filename = NetworkFileString(network)
    content = NetworkSpecFile(network)
    with open('networks/' + filename, 'w') as file:
      file.write(content)






