
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

def passive(node):
    """
    chooses the same edge that has been damaged, to be reinforced.
    this will be the baseline, where essentially the same weight-damage is inflicted 
    to the graph, but there is no counteraction.
    a trick to get the edge: find the node's neighbor that also has a budget max(budget A+budget b)
    """
    pool = []
    for curr in gi.neighbors(node):
        e = gi.get_edge(curr,node)
        bu1, bu2 =0,0
        bu1, bu2= e.source.budget, e.target.budget
        buds=[bu1,bu2]
        if None in buds:
            buds.remove(None)
        totbud= sum(buds)
        pool.append((totbud,e))       
    e_damaged,e = sorted(pool, key=lambda x: x[0])[-1]
    print pool
    print e_damaged
    return{e: node.budget}

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

