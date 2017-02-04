# QueryExperiments.py
# Bree Cummins and Shaun Harker
# MIT LICENSE
# 2017-02-03 

import DSGRN, json, time, datetime, sys

def LogToSTDOUT(string=''):
    """
    Print date and time, along with optional string input, to stdout.
    """
    if string: 
        string = ':\n' + str(string)
    else:
        string = ''
    print(str(datetime.datetime.now())+string)
    sys.stdout.flush()

def minute_passed(oldepoch):
    """
    Return true if at least one minute has passed since time.time()
    would have returned the input argument oldepoch
    """
    return time.time() - oldepoch >= 60

def QueryExperiment(database,gene,FP_OFF,FP_ON,savefilename=None,Log=LogToSTDOUT):
    """
    Perform Hysteresis query for each reduced parameter index 
    corresponding to "gene" for the provided "database". The
    "FP_OFF" and "FP_ON" define the quiescent and proliferative
    states, respectively, used to instantiate the HysteresisQuery
    object. Returns the number of matching reduced parameter indices.
    """

    # Log the network specification
    network_spec = database.network.specification()
    Log(network_spec)
    
    # Log start time
    Log('Beginning Experiment')

    # Get index of "gene"
    gene_index = database.network.index(gene)

    # Construct Query
    Log('Constructing Query')
    query = DSGRN.HysteresisQuery(database,gene,FP_OFF,FP_ON)
    Log('Query Construction Complete')

    # Determine number of reduced parameters
    N = query.GeneQuery.number_of_reduced_parameters()
    Log('There are ' + str(N) + ' reduced parameters.')

    # Loop through reduced parameters and call query
    count = 0
    epoch = time.time()
    for rpi in range(N):
      if query(rpi): count = count + 1
      if minute_passed(epoch):
        epoch = time.time()
        Log('Queries 0 through ' + str(rpi) + ' completed (with ' + str(count) + ' matches so far).')

    # Save query results to file
    if savefilename:
        with open(savefilename,'w') as f:
            json.dump( { network_spec : (N, count) }, f)

    # Return results
    return { network_spec : (N, count) }
