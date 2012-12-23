import environment
import config
import behaviour
import gi
import stats

from config import g

count_steps = 0

def wakeup_nodes(nodes):
    """
    wakes up the affected nodes for action. this will call 'behaviour'
    """
    for node in nodes:
        behaviour.node_method(node) # the action is defined there...

def step(): # what happens in each cycle. Main calls happen here.
    global count_steps
    count_steps += 1
    print "count_steps "+str(count_steps)
    nodes = environment.step()
    wakeup_nodes(nodes) # calls their behaviour, which calls the policy (what to do), and finally applies actions
    print "killed edges: "+str(stats.collector.num_kills)
    stats.snapshot()
    print "total graph weight:"+str(stats.collector.total_weight)
    stats.new_collector()

def termination_condition3():
    if gi.num_edges() <= 0:
        return True
    return False

def termination_condition():
    global count_steps
    if count_steps >= config.max_steps:
        return True
    return False

def initialize():
    """
    initialization procedures. For example: attaching methods to nodes.
    """
    global count_steps
    count_steps = 0
    stats.new_collector()
    for node in gi.nodes():
        if node is not None:
            setattr(node, "weight", 1.0)

def end():
    stats.write_history()

def run(gephi_stuff): # the Highest function
    global count_steps
    config.set_g(gephi_stuff['g'])
    config.set_gephi(gephi_stuff)
    initialize()
    while not termination_condition():
        step()
    end()

