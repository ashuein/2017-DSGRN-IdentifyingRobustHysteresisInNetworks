# draw_networks.py
# Shaun Harker
# 2018-01-26
# MIT LICENSE

# Overview:
#   Render all networks from a folder

# Command Line Arguments:
#   Argument 1: name of network folder 
#   Argument 2: name of image folder

import sys
import graphviz
import os

if __name__ == "__main__":

  if len(sys.argv) < 3:
    print("./draw_networks.py networkfolder imagefolder")
    exit(1)

  networkfolder = sys.argv[1]
  imagefolder = sys.argv[2]
  networks = [filename for filename in os.listdir(networkfolder)]
  networks.sort()
  for f in networks:
      network = DSGRN.Network( networkfolder + '/' + f)
      print(network.graphviz())
      x = graphviz.Source(network.graphviz(), filename= imagefolder + '/' + f + '.gv', format='png')
      x.render()