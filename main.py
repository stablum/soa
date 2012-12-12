import environment
import config
import behaviour
import gi
from config import g

def wakeup_nodes(damaged):
    """
    wakes up the affected nodes for action. this will call 'behaviour'
    """
    print "main.wakeup_nodes!"
    waking_nodes = set()
    for e in damaged:
        waking_nodes.add(e.source)
        waking_nodes.add(e.target)
    for node in waking_nodes:
        behaviour.node_method(node) # the action is defined there...

def step(): # what happens in each cycle. Main calls happen here.
    print "main.step!"
    damaged = environment.compute()
    environment.budgetize(damaged)
    wakeup_nodes(damaged) # calls their behaviour, which calls the policy (what to do), and finally applies actions
    snapshot()

def termination_condition():
    print "main.termination_condition!"
    for e in gi.edges():
        if len(gi.nodes()) < config.init_num_nodes:
            return True
    return False

def snapshot():
    pass #TODO statistics, screenshot, indicators calculations...

def initialize():
    """
    initialization procedures. For example: attaching methods to nodes.
    """
    print "main.initialize!"
    for node in gi.nodes():
        print node
        if node is not None:
            setattr(node, "weight", 1.0)

def run(_g): # the Highest function
    print "main.run!"
    config.set_g(_g)
    initialize()
    while not termination_condition():
        print "termination condition:",termination_condition()
        step()

