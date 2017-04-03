# Enqueue.py
# Shaun Harker
# 2017-04-02
# MIT LICENSE

# Enqueue jobs for Query paper on a cluster

import subprocess

jobs = [ 'qsub QueryPaperShard.sh ' + str(i) + ' ' + str(min(i+100000,212103360L
)) for i in range(0, 212103360L, 100000L)]

for job in jobs:
    subprocess.call(job, shell=True)
