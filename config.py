frac_edges = 0.1
frac_damage = 0.65
factor_reuse = 0.25
policy_id = 'simple'
init_num_nodes = 0 # set by set_g

_g = None

def g():
    global _g
    return _g

def set_g(__g):
    global _g
    global init_num_nodes
    _g = __g
    print "config.g is now ",type(g)
    init_num_nodes = len(g().nodes)

