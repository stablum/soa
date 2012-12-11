"""
abstraction for access to graph ('g'). So that the specific implementation is somewhat isolated
and that we don't have to handle complicated type conversions in our code.
"""
from config import g

def nodes():
    return [ node 
             for node 
             in g().nodes 
             if node is not None 
    ]

def edges():
    return list(g().edges)

