# external libraries
import random
import copy
import math
import gi

# local imports
import config
from config import g

def compute_edges():
    """ actions performed by the environment
        Alzeihmer desease:
        select randomly a certain percentage of edges. 
        The weights of the edges will be reduced
        of a certain percentage
    """
    print "environment.compute!"
    num_edges_selected = int(math.ceil(gi.num_edges() * config.frac_edges ))
    selected=gi.random_edges(num_edges_selected)
    damaged = set()
    for e in selected: # each of these edges will be assigned a damage
        prev_weight = e.weight
        e.weight = prev_weight * config.frac_damage
        diff = prev_weight - e.weight
        e.damage = diff # if the edge is too light, destroy it
        damaged.add(e)
    return damaged

def affected_nodes(damaged):
    waking_nodes = set()
    for e in damaged:
        waking_nodes.add(e.source)
        waking_nodes.add(e.target)
    return waking_nodes

def budgetize(damaged):
    """
    generates budgets for the nodes involved in the damaged edges.
    As some weight is removed, a part of this weight is given as a budget to the involved nodes.
    This weight can then be applied to strengtehn other nodes' edges. (this is done by the 'behaviour' func)
    the overall idea: some of the weight is lost, some is 'shifted' to other edges
    """
    print "environment.budgetize!"
    for e in damaged: # reset previous budgets. each cycle is a new story!
        e.source.budget = 0
        e.target.budget = 0
    
    for e in damaged: # a fraction of the edge's removed-weight becomes edges budget
        budget = e.damage * config.factor_reuse
        e.source.budget += budget 
        e.target.budget += budget
		
# TODO initialize custom fields
def kill_edges(damaged):
    for e in gi.edges():
        if e.weight < config.treshold_kill: #del e # FIXME!! careful!!!
            gi.kill_edge(e)

def step():
    damaged = compute_edges()
    nodes = affected_nodes(damaged)
    budgetize(damaged)
    kill_edges(damaged)
    return nodes
