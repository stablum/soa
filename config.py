frac_edges = 0.1
frac_damage = 0.65
factor_reuse = 0.25
policy_id = 'simple'
init_num_nodes = 0 # set by set_g

g = None

def set_g(_g):
    global g
    global init_num_nodes
    g = _g
    print "config.g is now ",type(g)
    init_num_nodes = len(g.nodes)

