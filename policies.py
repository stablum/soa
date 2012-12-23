import gi

def pro_poor(node):
    pool = []
    for curr in gi.neighbors(node):
        e = gi.get_edge(curr,node)
        pool.append((gi.edge_importance(e),e))
    importance,e = sorted(pool, key=lambda x: -x[0])[-1]
    return {e: node.budget}

def pro_rich(node):
    pool = []
    for curr in gi.neighbors(node):
        e = gi.get_edge(curr,node)
        pool.append((gi.edge_importance(e),e))
    importance,e = sorted(pool, key=lambda x: x[0])[-1]
    return {e: node.budget}

def simple(node):
    """
    chooses a random edge and returns the action that
    represents an increase of its weight, according to the budget.
    returns a request for increasing the weight of 
    edge e in the amount of the total budget
    """
    n = gi.random_neighbor(node) #hood
    e = gi.get_edge(n,node)
    return {e: node.budget}

#TODO: Policy_shortpath
#TODO: Policy_prorich
#TODO: Policy_propoor
#TODO: Policy_proheavy
#TODO: Policy_prolight
#TODO: Policy_proweightrich
#TODO: Policy_proweightpoor

def get(name):
    """
    returns the policy specified by the given name
    """
    return globals()[name]
    print x

