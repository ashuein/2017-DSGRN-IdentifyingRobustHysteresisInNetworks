# 02_Experiment.py
# Bree Cummins and Shaun Harker
# MIT LICENSE
# 2017-02-03 

from QueryExperiments import *

dbfile = "/share/data/CHomP/Projects/DSGRN/DB/data/6D_2016_08_26_cancerE2Fnetwork1.db"
savefilename="02_Experiment.json"
gene = "S"
FP_OFF={"E2F":[0,0],"E2F_Rb":[1,1]} 
FP_ON={"E2F":[1,8],"E2F_Rb":[0,0]}
database = DSGRN.Database(dbfile)
QueryExperiment(database, gene, FP_OFF, FP_ON, savefilename)
