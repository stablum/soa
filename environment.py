# external libraries
import random
import copy
import math

# local imports
import config

def environment():
    """ actions performed by the environment
        Alzeihmer desease:
        select randomly a certain percentage of edges. 
        The weights of the edges will be reduced
        of a certain percentage
    """
    edges_copy = copy.copy(g.edges)
    num_edges_selected = int(math.ceil(len(edges_copy) * config['frac_edges'] ))
    selected=random.sample(g.edges,num_edges_selected)
    damaged = set()
    for e in selected: # each of these edges will be assigned a damage
        prev_weight = e.weight
        e.weight = prev_weight * config['frac_damage']
        diff = prev_weight - e.weight
        e.damage = diff # if the edge is too light, destroy it
        if e.weight < 1.0: #del e # FIXME!! careful!!!
		    print e
    damaged.add(e)
    return damaged

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
        budget = e.damage * config['factor_reuse']
        e.source.budget += budget 
        e.target.budget += budget

		
def wakeup_nodes(damaged):
    """
    wakes up the affected nodes for action. this will call 'behaviour'
    """
    waking_nodes = set()
    for e in damaged:
	waking_nodes.add(e.source)
	waking_nodes.add(e.target)
    for node in waking_nodes:
        node.behavior() # the action is defined there...!!FIXME!!at moment bheaviour is not a method for node


def termination_condition():
    for e in g.edges:
	if len(g.nodes)<config['init_num_nodes']:
		return True
    return False

def snapshot():
    pass #TODO statistics, screenshot, indicators calculations...


# TODO initialize custom fields

