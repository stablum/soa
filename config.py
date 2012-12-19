import utils

frac_edges = 0.1
frac_damage = 0.65
factor_reuse = 0.25
policy_id = 'pro_rich'
init_num_nodes = 0 # set by set_g
max_steps = 100
treshold_kill = 0.2
_g = None
gephi = None

def g():
    global _g
    return _g

def gephi():
    global _gephi
    return _gephi

def set_g(__g):
    print "config.set_g!"
    global _g
    global init_num_nodes
    _g = __g
    print "config.g is now ",type(g)
    init_num_nodes = len(g().nodes)

def set_gephi(gephi_stuff):
    """
    sets all variables in the gephi environment
    """
    global gephi
    gephi = utils.Struct(**gephi_stuff)

