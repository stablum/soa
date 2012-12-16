import policies
import config
import gi

def apply_actions(self,actions):
    for e,increase in actions.items():
        self.budget -= increase
        if self.budget < 0.0:
            raise Exception("programming error: budget can not be < 0.0")
        gi.add_weight(e, increase)

def node_method(self):
    """
    behavior of the node agent:
    select one (or more?) of its edges to be reinforced,
    according to the node's budget. budget itself is a fraction 
    of the damage inflicted to the nodes' edges
    """
    actions = policies.get(config.policy_id)(self)
    apply_actions(self,actions)

