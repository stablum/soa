import utils

frac_edges = 0.1
frac_damage = 0.65
factor_reuse = 0.25
policy_id = 'pro_rich'
init_num_nodes = 0 # set by set_g
max_iterations = 320
treshold_kill = 0.2
#mypath = "D:\\ELECTIVES\\SELF_ORGA\\new_code\\" # CHANGE ME!
mypath = "C:\\soa\\" 
#stats_filename = mypath +"stats_"+policy_id+".csv" 
stats_filename = mypath +"stats.csv" 
runs_per_series = 100


_g = None
gephi = None

def g():
    global _g
    return _g

def gephi():
    global _gephi
    return _gephi

def set_g(__g):
    global _g
    global init_num_nodes
    _g = __g
    init_num_nodes = len(g().nodes)

def set_gephi(gephi_stuff):
    """
    sets all variables in the gephi environment
    """
    global gephi
    gephi = utils.Struct(**gephi_stuff)

