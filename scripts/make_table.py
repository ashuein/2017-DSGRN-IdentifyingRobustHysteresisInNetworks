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

  csv_file_string = "network,percent_hysteresis,percent_resettable_bistability,time\n"
  for key in sorted(X):
    rpi = float(X[key]["reduced_param_indices"])
    h_match = float(X[key]["hysteresis_matches"])
    r_match = float(X[key]["resettable_matches"])
    h_time = float(X[key]["time_to_compute_hysteresis"])
    r_time = float(X[key]["time_to_compute_resettable"])
    csv_file_string += key + "," + str(100.0 *h_match / rpi) + "," + str(100.0 * r_match / rpi) + "," + str(h_time + r_time) + "\n"

  md_file_string = " | network | Percent hysteresis match | Percent resettable bistability match | time |\n"
  md_file_string +=" | ------- | ------------------------ | ------------------------------------ | ---- |\n"
  for key in sorted(X):
    rpi = float(X[key]["reduced_param_indices"])
    h_match = float(X[key]["hysteresis_matches"])
    r_match = float(X[key]["resettable_matches"])
    h_time = float(X[key]["time_to_compute_hysteresis"])
    r_time = float(X[key]["time_to_compute_resettable"])
    md_file_string += key + "|" + str(100.0 *h_match / rpi) + "% | " + str(100.0 * r_match / rpi) + "% | " + str(h_time + r_time) + " |\n"

  with open(csv_filename, 'w') as outfile:
    outfile.write(csv_file_string)

  with open(md_filename, 'w') as outfile:
    outfile.write(md_file_string)
