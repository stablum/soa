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
    print "average path length, see note1:"+ str(stats.collector.path_length)
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

def initialize_exp():
    """
    initialization procedures. For example: attaching methods to nodes.
    """
    global count_steps
    count_steps = 0
    stats.new_collector()
    gi.save_weights()

def end_exp():
    print "note1: avg path length reports harmonic mean of all shortest path"
    print "shor.path are chosen favouring high weights"
    print "(mathematically the distance minimized between 2nodes is the sum of the inverse of the weights the edge crossed)"
    print "avg. path length reports now the sum of the real weights. the bigger, the better"
    gi.restore_weights()

def run_exp():
    initialize_exp()
    while not termination_condition():
        step()
    end_exp()

def run(gephi_stuff): # the Highest function (hehe)
    config.set_g(gephi_stuff['g'])
    config.set_gephi(gephi_stuff)
    gi.save_weights()
    for exp_num in range(0, config.exps_per_run):
        stats.exp_num = exp_num
        run_exp()
    stats.write_history()

