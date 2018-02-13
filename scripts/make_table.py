# make_table.py
# Shaun Harker
# 2017-04-28
# MIT LICENSE

# Overview:
#   Read the summary.json file and produce a markdown table from it

# Command Line Arguments:
#   Argument 1: name of summary.json file. 
#   Argument 2: name of output csv file
#   Argument 3: name of output md file

import json

import sys

if __name__ == "__main__":
  if len(sys.argv) < 4:
    print("./parse_summary.py summary.json summary.csv summary.md")
    exit(1)

  filename = sys.argv[1]
  csv_filename = sys.argv[2]
  md_filename = sys.argv[3]

  with open(filename) as infile:
    data = infile.read()

  X = json.loads(data)

  csv_file_string = "network,percent_partial_path_hysteresis,percent_partial_path_resettable_bistability,percent_full_path_hysteresis,percent_full_path_resettable_bistability,time\n"
  md_file_string = "| network | figure | partial path hysteresis match | partial path resettable bistability match |  full path hysteresis match | full path resettable bistability match | time |\n"
  md_file_string +="| ------- | ------ | ------------------------ | ------------------------------------ | ---- | ---- | ---- |\n"
  for key in sorted(X):
    rpi = float(X[key]["reduced_param_indices"])
    ph_match = float(X[key]["partial_hysteresis_matches"])
    ph_param = float(X[key]["partial_hysteresis_params"])
    pr_match = float(X[key]["partial_resettable_matches"])
    pr_param = float(X[key]["partial_resettable_params"])
    ph_time = float(X[key]["time_to_compute_partial_hysteresis"])
    pr_time = float(X[key]["time_to_compute_partial_resettable"])
    fh_match = float(X[key]["full_hysteresis_matches"])
    fh_param = float(X[key]["full_hysteresis_params"])
    fr_match = float(X[key]["full_resettable_matches"])
    fr_param = float(X[key]["full_resettable_params"])
    fh_time = float(X[key]["time_to_compute_full_hysteresis"])
    fr_time = float(X[key]["time_to_compute_full_resettable"])
    ph_ratio = str(100.0 * ph_match / ph_param) 
    pr_ratio = str(100.0 * pr_match / pr_param) 
    fh_ratio = str(100.0 * fh_match / fh_param) 
    fr_ratio = str(100.0 * fr_match / fr_param) 
    t = str(ph_time + pr_time + fh_time + fr_time)
    csv_file_string += key + "," + ph_ratio + "," + pr_ratio + "," + fh_ratio + ", " + fr_ratio + ", " + t + "\n"
    md_file_string += key + "| ![](./" + key + ".gv.png) |" + ph_ratio + "% | " + pr_ratio + "% | " + fh_ratio + "% | " + fr_ratio + "% | " +  t + " |\n"

  with open(csv_filename, 'w') as outfile:
    outfile.write(csv_file_string)

  with open(md_filename, 'w') as outfile:
    outfile.write(md_file_string)
