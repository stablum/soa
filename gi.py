"""
abstraction for access to graph ('g'). So that the specific implementation is somewhat isolated
and that we don't have to handle complicated type conversions in our code.
"""
from config import g
import random

def nodes():
    return [ node 
             for node 
             in g().nodes 
             if node is not None 
    ]

def edges():
    return list(g().edges)

def neighbors(node):
    ret = []
    for n in node.neighbors:
        print "neighbor:"+str(n)
        if n is not None:
            ret.append(n)
    return ret
    
def random_neighbor(node):
    tmp = neighbors(node)
    random.shuffle(tmp)
    return tmp[0]
    