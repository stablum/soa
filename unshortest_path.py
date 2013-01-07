# the following should be copy pasted
# problem: currently this algorythm favour shortest path with low weight rather than high
# solution (with bugs to be fixed): favour high  weight by adding the opposite of the weight 1./ e.weight
# this way: high weight = good easy connection
# buggy: does not seem to behave well, hilights only last steps of the path. try it out...
class Punto:
    pass

def unshortest_path(start, end):
    # initialize distances and predecessor edges
    all_edges=g.edges # gi.edges()#    damaged= start ? end#if len(damaged) !=0:#    all_edges.discard(damaged.pop())
    dist, prev = {}, {}
    for v in g.nodes:
        dist[v], prev[v] = float('inf'), None
    dist[start] = 0
    for i in range(len(g.nodes)):   # Bellman-Ford algorithm, tweaked so that high weight = faster 
        for e in all_edges: # TODO: exclude from the count the original AB
            if dist[e.target] > dist[e.source] + 1./ e.weight: #... + 1./ e.weight
                dist[e.target] = dist[e.source] + 1./ e.weight #... + 1./ e.weight
                prev[e.target] = e
                print ( i, e.source, e.target, e.weight, '         ', e)
                if e.source==start or e.target ==start:
                    print ('!!!!!!', e.source,e.target, prev[e.source], prev[e.target])
                    prev[start]=e
            if dist[e.source] > dist[e.target] + 1./ e.weight: #... + 1./ e.weight
                dist[e.source] = dist[e.target] + 1./ e.weight  #... + 1./ e.weight
                prev[e.source] = e
                print ( i, e.source, e.target, e.weight, '         ', e)
                if e.target==start or e.source ==start:
                    print ('!!!!!!', e.source, e.target, prev[e.source],prev[e.target])
    print('prev(start) + prev(end)', prev[start], prev[end])
    for v in g.nodes:# color all the nodes and edges as RGB 200, 200, 200
        v.color = color(200, 200, 200)
    for e in g.edges:
        e.color = color(200, 200, 200)
    vv=end #e_path, v_path, w_path=[],[],[]
    mypath=Punto()
    mypath.v, mypath.e, mypath.w, mypath.winv =[],[],[],[]
    start.color=green
    while vv != start:
        e=prev[vv]
        mypath.v.append(vv)
        mypath.e.append(e)
        mypath.w.append(e.weight)
        mypath.winv.append(1./e.weight)
        vv.color=green
        e.color=green
        s,t =e.source, e.target
        if vv==s:
            vv=t
        else:
            vv=s
    return (dist[end], prev, dist,mypath)   # return the total weight of the path (distance)
 
[a,prev,dist,mypath]=unshortest_path(v33, v67)