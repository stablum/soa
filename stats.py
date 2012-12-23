from utils import Struct
import gi

collector = None
history = []

def new_collector_dict():
    """
    returns the dict that describes the current data collection "snapshot"
    """
    ret = {
        'num_kills':0,
        'total_weight':0
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

def snapshot():
    """ statistics and stuff (??) """
    global collector
    collector.total_weight = total_weight()

