import gi
import utils

def init_dist(nodes):
    """
    initialize dist matrix
    """
    dist = {}
    for v in nodes:
        dist[v] = {}
        for v2 in nodes:
            dist[v][v2] = float('Inf')
    return dist

def run(nodes,edges):
    """
    execute the Floyd Warshall algorithm
    """
    dist = init_dist(nodes)
    
    # set matrix identity elements to 0
    for v in nodes:
        dist[v][v] = 0
    
    # fill matrix with intial edge weights
    for e in edges:
        # shorter in our case means with stronger connections, hence:
        
        w = gi.get_weight(e)
        if w > 0:
            d = 1.0 / w
        else:
            d = 99999 # "Inf"

        # inizialization of v->u and u->v to same value because the graph is undirected
        dist[e.source][e.target] = d
        dist[e.target][e.source] = d
            

    # the core of the algorithm
    for v1 in nodes:
        for v2 in nodes:
            for v3 in nodes:
                if dist[v2][v1] + dist[v1][v3] < dist[v2][v3]:
                    dist[v2][v3] = dist[v2][v1] + dist[v1][v3]
    return dist

def list_dist(dist):
    """
    converts the matrix of distances to a list
    """
    ret = []
    for v_stuff in dist.values():
        for d in v_stuff.values():
            ret.append(d)
    return ret

def avg(dist):
    """
    calculates the average path length
    """

    # from matrix to list
    tmp = list_dist(dist)
    filtered = filter(lambda x: x > 0.0 and x < float('Inf'), tmp)
    return utils.harmean(filtered)

