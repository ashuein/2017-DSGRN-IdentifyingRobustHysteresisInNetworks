# 00_Experiment.py
# Bree Cummins and Shaun Harker
# MIT LICENSE
# 2017-02-03 

from QueryExperiments import *

dbfile = "00_Experiment.db"
savefilename="00_Experiment.json"
gene = "X1"
FP_OFF={"X1":0,"X2":0,"X3":0} 
FP_ON={"X1":[1,3],"X2":[1,2],"X3":[1,1]} 
QueryExperiment(dbfile, gene, FP_OFF, FP_ON, savefilename)
