def unshortest_path(start, end):
    # initialize distances and predecessor edges
    all_edges=g.edges # gi.edges()#    damaged= start ? end#if len(damaged) !=0:#    all_edges.discard(damaged.pop())
    dist, prev = {}, {}
    for v in g.nodes:
        dist[v], prev[v] = float('inf'), None
    dist[start] = 0
    for i in range(len(g.nodes)+1):   # Bellman-Ford algorithm, tweaked so that high weight = faster 
        for e in all_edges: # TODO: exclude from the count the original AB
            if dist[e.target] > dist[e.source] + e.weight: #1/
                dist[e.target] = dist[e.source] + e.weight
                prev[e.target] = e
                print ( i, e.source, e.target, e.weight, '         ', e)
            if dist[e.source] > dist[e.target] + e.weight: #1/
                dist[e.source] = dist[e.target] + e.weight
                prev[e.source] = e
                print ( i, e.source, e.target, e.weight, '         ', e)
    print ('dist=', dist)
    print ('prev=', prev)
    print('prev(start) + prev(end)', prev[start], prev[end])
    for v in g.nodes:# color all the nodes and edges as RGB 200, 200, 200
        v.color = color(200, 200, 200)
    for e in g.edges:
        e.color = color(200, 200, 200)
    return (dist[end])   # return the total weight of the path (distance)
 
 unshortest_path(v33, v11)
 
    if dist[end] < float('inf'):    # highlight a shortest path with the green color (if one exists)
        e = prev[end]
        end.color = green
        print ("painting", e)
        while e != None: #while
            if e!=None:
                e.color = green
                e.source.color = green
                print (e.source, e.target, prev[e.source])
                if prev[e.source]!=None:
                    e = prev[e.source]

unshortest_path(v33, v11)
