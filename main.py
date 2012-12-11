
def step(): # what happens in each cycle. Main calls happen here.
    damaged = environment()
    budgetize(damaged)
    wakeup_nodes(damaged) # calls their behaviour, which calls the policy (what to do), and finally applies actions
    snapshot()

def run(): # the Highest function
    while not termination_condition():
	print termination_condition()
	step()
