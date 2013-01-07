from utils import Struct
import gi
import config
import shorpath

collector = None
history = []

def new_collector_dict():
    """
    returns the dict that describes the current data collection "snapshot"
    """
    ret = {
        'num_kills':0,
        'total_weight':0,
        'path_length':0
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
    collector = Struct(**args)
    
    return collector

def total_weight():
    ret = 0.0
    for e in gi.edges():
        ret += gi.get_weight(e)
    return ret

def path_length():
    ret = 0.0
    ret += shorpath.getpl()
    return ret

def snapshot():
    """ statistics and stuff (??) """
    global collector
    collector.total_weight = total_weight()
    collector.path_length=path_length()

def write_history():
    """ write statistics on a file
        this should be called at the end """
    global history
    f = open(config.stats_filename, 'w')
    f.write("num_kills,total_weight\n,pathlength")
    for c in history:
        print c
        f.write(str(c.num_kills)+","+str(c.total_weight)+"\n"+","+str(c.path_length))
        f.flush()
    f.close()

