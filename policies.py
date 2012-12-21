import gi

def pro_rich(node):
    pool = []
    for curr in gi.neighbors(node):
        pool.append((gi.weighted_degree(curr),curr))
    wd,n2 = sorted(pool, key=lambda x: x[0])[-1]
    e = gi.get_edge(n2,node)
    w = gi.get_weight(e)
    print (w*0.25)
    return {e: w*0.25}

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

