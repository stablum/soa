# external libraries
import random
import math

# local imports
import gi
import config
from config import g
import stats

def compute_edges():
    """ actions performed by the environment
        Alzeihmer desease:
        select randomly a certain percentage of edges. 
        The weights of the edges will be reduced
        of a certain percentage
    """
    num_edges_selected = int(math.ceil(gi.num_alive_edges() * config.frac_edges ))
    selected=gi.random_edges(num_edges_selected)
    damaged = set()
    thisdamage=[]
    for e in selected: # each of these edges will be assigned a damage
        prev_weight = gi.get_weight(e)
        gi.mult_weight(e, config.frac_damage)
        diff = prev_weight - e.weight
        e.damage = diff # if the edge is too light, destroy it
        thisdamage.append((e.source, e.target, e.damage))
        if gi.get_weight(e) < 1.0: #del e # FIXME!! careful!!!
            pass
        damaged.add(e)
    return damaged

def affected_nodes(damaged):
    waking_nodes = set()
    for e in damaged:
        waking_nodes.add(e.source)
        waking_nodes.add(e.target)
    if None in waking_nodes:
        waking_nodes.remove(None)
    return waking_nodes

def budgetize(damaged):
    """
    generates budgets for the nodes involved in the damaged edges.
    As some weight is removed, a part of this weight is given as a budget to the involved nodes.
    This weight can then be applied to strengtehn other nodes' edges. (this is done by the 'behaviour' func)
    the overall idea: some of the weight is lost, some is 'shifted' to other edges
    """
    for e in damaged: # reset previous budgets. each cycle is a new story!
        e.source.budget = 0
        e.target.budget = 0
    
    for e in damaged: # a fraction of the edge's removed-weight becomes edges budget
        budget = e.damage * config.factor_reuse
        e.source.budget += budget 
        e.target.budget += budget

# TODO initialize custom fields
def kill_edges(damaged):
    for e in gi.alive_edges():
        if e.weight < config.treshold_kill: #del e # FIXME!! careful!!!
            gi.kill_edge(e)
            stats.collector.num_kills += 1

def step():
    damaged = compute_edges()
    nodes = affected_nodes(damaged)
    budgetize(damaged)
    kill_edges(damaged)
    return nodes

