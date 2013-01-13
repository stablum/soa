import utils

from org.gephi.statistics.plugin import GraphDistance
import gi
import config
import shorpath

collector = None
history = []
exp_num = 0
exp_timestamp = utils.now_timestamp()

def new_collector_dict():
    """
    returns the dict that describes the current data collection "snapshot"
    """
    global exp_num
    ret = {
        'num_kills':0,
        'total_weight':0,
        'path_length':0,    # http://gephi.org/docs/toolkit/org/gephi/statistics/plugin/GraphDistance.html#getPathLength()
        'exp_num':exp_num,
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
    collector.mean_edges_importance=mean_edges_importance()
    collector.std_edges_importance=std_edges_importance()

def write_history():
    """ write all statistics stored in memory on a csv file.
        *overwrites* previous file"""
    global history
    global exp_num
    print "write_history; the exp_num is now:"+str(exp_num)+"\n"
    f = open(config.stats_filename, 'w')
    f.write("num_kills,total_weight,path_length,exp_num\n,mean_edges_importance,std_edges_importance")
    for c in history:
        f.write(str(c.num_kills)+","+str(c.total_weight)+","+str(c.path_length)+","+str(c.exp_num)+"\n" +","+str(c.mean_edges_importance)+","+str(c.std_edges_importance))
        f.flush()
    f.close()

