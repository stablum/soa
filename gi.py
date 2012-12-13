"""
abstraction for access to graph ('g'). So that the specific implementation is somewhat isolated
and that we don't have to handle complicated type conversions in our code.
"""
from config import g
import random

def nodes():
    """
    returns the graph's nodes
    """
    return [ node 
             for node 
             in g().nodes 
             if node is not None 
    ]

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

def num_edges():
    """
    returns the how many edges are there
    """
    return len(edges())
    
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
    return tmp[0]

def random_edges(how_many):
    """ 
    returns some edges, randomly selected
    """
    how_many = min(how_many,num_edges())
    ret=random.sample(edges(),how_many)
    return ret

def kill_edge(e):
    g().underlyingGraph.readUnlockAll()
    del e

