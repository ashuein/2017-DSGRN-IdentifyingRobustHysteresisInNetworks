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
with open('results.txt') as infile:
  lines = infile.readlines()

lines = [ line for line in lines if line.strip() ]  # remove empty lines
lines = [ line for i, line in enumerate(lines) if i%2 == 1 ] # odd lines
lines = [ line.split()[0] for line in lines ] # first entry in line

N = len(lines)/6

s = '{'
for i in range(0,N):
  if i > 0:
    s += ", "
  s += '"' + lines[6*i+0] + '" : { '
  s += ' "reduced_param_indices" : ' + lines[6*i+1] + ', '
  s += ' "time_to_compute_hysteresis" : ' + lines[6*i+2] + ', '
  s += ' "time_to_compute_resettable" : ' + lines[6*i+3] + ', '
  s += ' "hysteresis_matches" : ' + lines[6*i+4] + ', '
  s += ' "resettable_matches" : ' + lines[6*i+5] + '}'
s += '}'

print(s)
