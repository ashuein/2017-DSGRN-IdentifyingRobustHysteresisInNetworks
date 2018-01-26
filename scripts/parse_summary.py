# parse_summary.py
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Read the summary.txt file and produce a json file from it
# Command Line Arguments:
#   Argument 1: name of summary.txt file. 

# Example summary.txt file:

# Network:
# network_2a2b8
# Number of reduced parameter indices = 
# 180351360
# Time to compute hysteresis query (in seconds):
# 886531
# Time to compute resettable bistability query (in seconds):
# 880204
# Number of hysteresis matches = 
# 170324 computations/network_2a2b8_hysteresis.txt
# Number of resettable bistability matches = 
# 5246268 computations/network_2a2b8_resettable.txt
#
# ...repeat...

import sys

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("./parse_summary.py summary.txt")
    exit(1)

  filename = sys.argv[1]

  with open(filename) as infile:
    lines = infile.readlines()

  lines = [ line for line in lines if line.strip() ]  # remove empty lines
  lines = [ line for i, line in enumerate(lines) if i%2 == 1 ] # odd lines
  lines = [ line.split() for line in lines ]

  N = len(lines)/6

  s = '{'
  for i in range(0,N):
    if i > 0:
      s += ", "
    s += '"' + lines[6*i+0][0] + '" : { '
    s += ' "reduced_param_indices" : ' + lines[6*i+1][0] + ', '
    s += ' "time_to_compute_hysteresis" : ' + lines[6*i+2][0] + ', '
    s += ' "time_to_compute_resettable" : ' + lines[6*i+3][0] + ', '
    s += ' "hysteresis_matches" : ' + lines[6*i+4][0] + ', '
    s += ' "hysteresis_params" : ' + lines[6*i+4][1] + ', '
    s += ' "resettable_matches" : ' + lines[6*i+5][0] + ', '
    s += ' "resettable_params" : ' + lines[6*i+5][1] + '}'
  s += '}'

  print(s)
