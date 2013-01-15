import utils

from org.gephi.statistics.plugin import GraphDistance
import gi
import config
import shorpath
import main
import os

collector = None
history = []
run_num = 0
run_timestamp = utils.now_timestamp()

def infer_stats_filename():
    return config.stats_filename#.replace(".csv","_"+config.policy_id+".csv")

def new_collector_dict():
    """
    returns the dict that describes the current data collection "snapshot"
    """
    ret = {
        'count_iterations':main.count_iterations,
        'num_kills':0,
        'total_weight':0,
        'path_length':0,    # http://gephi.org/docs/toolkit/org/gephi/statistics/plugin/GraphDistance.html#getPathLength()
        'run_num':run_num,
        'mean_edges_importance':0,
        'std_edges_importance':0
    }
    return ret

def new_collector():
    """
    create a new data snapshot.
    it will be filled from the other components.
    """
    print "stats.new_collector!"
    global collector
    args = new_collector_dict()
    if collector is not None:
        history.append(collector)
    collector = utils.Struct(**args)
    
    return collector

def total_weight():
    ret = 0.0
    for e in gi.edges():
        ret += gi.get_weight(e)
    return ret

def path_length():
    ret = 0.0 # FIXME
    ret += shorpath.getpl()
    return ret

def mean_edges_importance():
    ret = 0.0 # new
    ret += gi.get_mean_edges_importance()
    return ret    

def std_edges_importance():
    ret = 0.0 # new
    ret += gi.get_std_edges_importance()
    return ret 

def snapshot():
    """ statistics and stuff (??) """
    global collector
    collector.total_weight = total_weight()
    collector.path_length = path_length()
    edges_importances = gi.get_all_edges_importances()
    collector.mean_edges_importance=utils.mean(edges_importances)
    collector.std_edges_importance=utils.std(edges_importances)

def get_run_num_offset():
    if os.path.exists(infer_stats_filename()):
        ret = get_last_saved_run_num() + 1
    else:
        ret = 0
    return ret

def write_history():
    """ write all statistics stored in memory on a csv file.
        *overwrites* previous file"""
    global history
    global run_num
    global count_iterations
    print "write_history; the run_num is now:"+str(run_num)+"\n"
    global collector #mik

    run_num_offset = get_run_num_offset()
    f = open(infer_stats_filename(), 'a')
    if run_num_offset == 0:
        f.write("count_iterations,num_kills,total_weight,path_length,run_num,mean_edges_importance,std_edges_importance\n")
        f.flush()
    for c in history: #+c.run_num DELETED
        f.write(str(c.count_iterations)+","+str(c.num_kills)+","+str(c.total_weight)+","+str(c.path_length)+","+str(run_num_offset)+","+str(c.mean_edges_importance)+","+str(c.std_edges_importance)+"\n")
        f.flush()
    f.close()
    del (collector, history)
    collector = None
    history = [] #mik

def get_last_saved_run_num():
    """
    returns the last saved run number
    """
    f = open(infer_stats_filename(), 'r')
    last_line = f.readlines()[-1]
    f = open(infer_stats_filename(), 'r') #startmik
    first_line = f.readlines()[0] 
    if last_line==first_line:
        ret=0
    else:
        ret = int(last_line.split(",")[4]) # endmik
    f.close()
    return ret

