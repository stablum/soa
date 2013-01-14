import environment
import config
import behaviour
import gi
import stats

from config import g

count_iterations = 0

def wakeup_nodes(nodes):
    """
    wakes up the affected nodes for action. this will call 'behaviour'
    """
    for node in nodes:
        behaviour.node_method(node) # the action is defined there...

def iteration_counter(): # this gets launched by stats
    global count_iterations
    count_iterations +=1
    return count_iterations

def iteration(): # what happens in each cycle. Main calls happen here.
    global count_iterations
    print "count_iterations "+str(count_iterations)
    nodes = environment.step()
    wakeup_nodes(nodes) # calls their behaviour, which calls the policy (what to do), and finally applies actions
    print "killed edges: "+str(stats.collector.num_kills)
    stats.snapshot()
    print "total graph weight:"+str(stats.collector.total_weight)
    print "average path length, see note1:"+ str(stats.collector.path_length)
    print "mean edge importance:"+str(stats.collector.mean_edges_importance)
    print "std edge importance:"+str(stats.collector.std_edges_importance)

    stats.new_collector()

def termination_condition3():
    if gi.num_edges() <= 0:
        return True
    return False

def termination_condition():
    global count_iterations
    if count_iterations >= config.max_iterations:
        return True
    return False

def initialize_run():
    """
    initialization procedures. For example: attaching methods to nodes.
    """
    global count_iterations
    count_iterations = 0
    stats.new_collector()
    gi.save_weights()

def end_run():
    print "note1: avg path length reports harmonic mean of all shortest path"
    print "shor.path are chosen favouring high weights"
    print "(mathematically the distance minimized between 2nodes is the sum of the inverse of the weights the edge crossed)"
    print "avg. path length reports now the sum of the real weights. the bigger, the better"
    gi.restore_weights()

def simulation_run():
    initialize_run()
    while not termination_condition():
        iteration()
    end_run()

def series(gephi_stuff): # the Highest function (hehe)
    config.set_g(gephi_stuff['g'])
    config.set_gephi(gephi_stuff)
    gi.save_weights()
    for run_num in range(0, config.runs_per_series):
        stats.run_num = run_num
        simulation_run()
    stats.write_history()

