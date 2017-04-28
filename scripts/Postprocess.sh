#!/bin/bash

./scripts/CollateJobs.sh $1 > $1/summary.txt
python ./scripts/parse_summary.py  $1/summary.txt > $1/summary.json
python ./scripts/make_table.py $1/summary.json $1/table.md
