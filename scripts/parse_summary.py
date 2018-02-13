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
# Time to compute partial path hysteresis query (in seconds):
# 886531
# Number of partial path hysteresis matches = 
# 170324 computations/network_2a2b8_hysteresis.txt
# Time to compute partial path resettable bistability query (in seconds):
# 880204
# Number of partial path resettable bistability matches = 
# 5246268 computations/network_2a2b8_resettable.txt
# Time to compute full path hysteresis query (in seconds):
# 886531
# Number of full path hysteresis matches = 
# 170324 computations/network_2a2b8_hysteresis.txt
# Time to compute full path resettable bistability query (in seconds):
# 880204
# Number of full path resettable bistability matches = 
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

  N = len(lines)/10

  s = '{'
  for i in range(0,N):
    if i > 0:
      s += ", "
    s += '"' + lines[10*i+0][0] + '" : { '
    s += ' "reduced_param_indices" : ' + lines[10*i+1][0] + ', '
    s += ' "time_to_compute_partial_hysteresis" : ' + lines[10*i+2][0] + ', '
    s += ' "partial_hysteresis_matches" : ' + lines[10*i+3][0] + ', '
    s += ' "partial_hysteresis_params" : ' + lines[10*i+3][1] + ', '
    s += ' "time_to_compute_partial_resettable" : ' + lines[10*i+4][0] + ', '
    s += ' "partial_resettable_matches" : ' + lines[10*i+5][0] + ', '
    s += ' "partial_resettable_params" : ' + lines[10*i+5][1] + ', '
    s += ' "time_to_compute_full_hysteresis" : ' + lines[10*i+6][0] + ', '
    s += ' "full_hysteresis_matches" : ' + lines[10*i+7][0] + ', '
    s += ' "full_hysteresis_params" : ' + lines[10*i+7][1] + ', '
    s += ' "time_to_compute_full_resettable" : ' + lines[10*i+8][0] + ', '
    s += ' "full_resettable_matches" : ' + lines[10*i+9][0] + ', '
    s += ' "full_resettable_params" : ' + lines[10*i+9][1] + '}'
  s += '}'

  print(s)
