import environment
import config
import behaviour
import gi
from config import g

count_steps = 0

def wakeup_nodes(nodes):
    """
    wakes up the affected nodes for action. this will call 'behaviour'
    """
    print "main.wakeup_nodes!"
    for node in nodes:
        behaviour.node_method(node) # the action is defined there...

def step(): # what happens in each cycle. Main calls happen here.
    print "main.step!"
    global count_steps
    count_steps += 1
    print "count_steps "+str(count_steps)
    nodes = environment.step()
    wakeup_nodes(nodes) # calls their behaviour, which calls the policy (what to do), and finally applies actions
    snapshot()

def termination_condition3():
    print "main.termination_condition!"
    if gi.num_edges() <= 0:
        return True
    return False

def termination_condition():
    global count_steps
    print "main.termination_condition!"
    if count_steps >= config.max_steps:
        return True
    return False

def snapshot():
    pass #TODO statistics, screenshot, indicators calculations...

def initialize():
    """
    initialization procedures. For example: attaching methods to nodes.
    """
    global count_steps
    count_steps = 0
    print "main.initialize!"
    for node in gi.nodes():
        if node is not None:
            setattr(node, "weight", 1.0)

def run(_g): # the Highest function
    print "main.run!"
    config.set_g(_g)
    initialize()
    while not termination_condition():
        print "!!" + str(count_steps)
        print "termination condition:",termination_condition()
        step()

