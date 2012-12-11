import environment
import config

g = None # workaround for visibility of 'g'

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

def step(): # what happens in each cycle. Main calls happen here.
    damaged = environment.compute()
    environment.budgetize(damaged)
    wakeup_nodes(damaged) # calls their behaviour, which calls the policy (what to do), and finally applies actions
    snapshot()

def termination_condition():
    global g
    for e in g.edges:
	if len(g.nodes) < config.init_num_nodes:
		return True
    return False

def snapshot():
    pass #TODO statistics, screenshot, indicators calculations...

def run(_g): # the Highest function
    global g
    g = _g
    while not termination_condition():
	print termination_condition()
	step()
