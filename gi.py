"""
abstraction for access to graph ('g'). So that the specific implementation 
is somewhat isolated and that we don't have to handle complicated type 
conversions in our code.
"""
import random

from config import g
import utils

saved_weights = None

def nodes():
    """
    returns the graph's nodes
    """
    return [ node 
             for node 
             in g().nodes 
             if node is not None 
    ]

def random_node_i():
    return random.randint(0,len(nodes()) - 1)

def random_node():
    i = random_node_i()
    return nodes()[i]

def edges():
    """
    returns the graph's edges
    """
    return [ e 
            for e 
            in g().edges 
            if e is not None 
            and hasattr(e,'source')
            and hasattr(e,'target')
    ]

def alive_edges():
    """
    return a list of edges that have not been killed
    """
    return [ e for e in edges() if get_weight(e) > 0.0 ]

def num_edges():
    """
    returns the how many edges are there
    """
    return len(edges())

def num_alive_edges():
    """
    returns the how many edges are there
    """
    return len(alive_edges())
    
def num_nodes():
    return len(nodes())
    
def neighbors(node):
    """
    returns the neighbors of a node
    """
    ret = []
    for n in node.neighbors:
        if n is not None:
            ret.append(n)
    return ret
    
def random_neighbor(node):
    """
    returns a randomly selected node from
    the node's neighborhood
    """
    tmp = neighbors(node)
    random.shuffle(tmp)

    for n2 in tmp:
        # checking that an edge is actually there
        if has_edge(n2,node):
            return n2

    raise Exception("no neighbor found!")

def random_edges(how_many,only_alive=True): # FIXME: more elegant than parametrized?? Boh!
    """ 
    returns some edges, randomly selected
    """
    how_many = min(how_many,num_edges())

    pool = None
    if only_alive:
        pool = alive_edges()
    else:
        pool = edges()

    ret=random.sample(pool,how_many)
    return ret

def random_edge(alive=True):
    return random_edges(1,alive=alive)

def kill_edge(e):
    g().underlyingGraph.readUnlockAll()
    set_weight(e, 0.0)

def add_weight(e,increase):
    set_weight(e,get_weight(e) + increase)

def set_weight(e,weight):
    e.getEdge().getEdgeData().setWeight(weight)

def get_weight(e):
    return e.weight

def mult_weight(e, factor):
    set_weight(e, get_weight(e) * factor)
 
def has_edge(n1,n2):
    e = (n1 ? n2).pop() # take the edge linking 'node' to 'n'
    return False if e is None else True

def get_edge(n1,n2):
    e = (n1 ? n2).pop() # take the edge linking 'node' to 'n'
    if e is None:
        raise Exception("gi.get_edge("+str(n1)+","+str(n2)+") did not find the edge")
    return e

def node_edges(n1):
    ret = []
    for n2 in neighbors(n1):
        if has_edge(n1,n2):
            ret.append(get_edge(n1,n2))
    return ret

def weighted_degree(node):
    weights = [ get_weight(e) for e in node_edges(node) ]
    ret = sum(weights)
    return ret

def degree(node):
    return node.degree

def edge_importance(e):
    a = e.source
    b = e.target
    if not a and b:
        raise Exception("cannot calculate edge importance: missing edge target or edge source")
    wda = weighted_degree(a)
    wdb = weighted_degree(b)
    w_ab = get_weight(e)
    importance = 0.5 * w_ab * (wda + wdb)
    return importance

def get_all_edges_importance():
    return [edge_importance(e) for e in alive_edges()]

def get_weights_dict():
    ret = {}
    for e in edges():
        w = get_weight(e)
        ret[e] = w
    return ret

def save_weights():
    """ 
    function used to save (for a consequent restore) of the status of the graph (that is, weights of edges)
    """
    global saved_weights
    saved_weights = get_weights_dict()

def restore_weights_from_dict(d):
    for e,w in d.items():
        set_weight(e,w)

def restore_weights():
    """
    function that is complementar to save_weights(): restore the weights to the saved state
    """
    global saved_weights
    restore_weights_from_dict(saved_weights)

