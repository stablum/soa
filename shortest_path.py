def shortest_path(start, end):
    # initialize distances and predecessor edges
    all_edges=g.edges # gi.edges()
    damaged= start ? end
    if len(damaged) !=0:
        all_edges.discard(damaged.pop())
    dist, prev = {}, {}
    sp_nodes, sp_edges=set([]),set([])
    for v in g.nodes:
        dist[v], prev[v] = float('inf'), None
    dist[start] = 0
    for i in range(len(g.nodes)):   # Bellman-Ford algorithm, tweaked so that high weight = faster 
        for e in all_edges: # TODO: exclude from the count the original AB
            if dist[e.target] > dist[e.source] + e.weight: #1/
                dist[e.target] = dist[e.source] + e.weight
                prev[e.target] = e
                print ( i, e.source, e.target, e.weight, '         ', e)
    for v in g.nodes:# color all the nodes and edges as RGB 200, 200, 200
        v.color = color(200, 200, 200)
    for e in g.edges:
        e.color = color(200, 200, 200)
    if dist[end] < float('inf'):    # highlight a shortest path with the green color (if one exists)
        e = prev[end]
        end.color = green
        print e
        while e != None: #while
            e.color = green
            e.source.color = green
            e.target.color= green
            print (e.source, e.target, prev[e.source])
            e = prev[e.source]
    return (dist[end], prev, dist)   # return the total weight of the path (distance)

[a,prev,dist]=shortest_path(v33, v11)


if e.source == start e.target==start
    firstlaste.appen(e)
    
    #\def get_equal(in_set, in_element):
   for element in in_set:
       if element == in_element:
           return element
   return None

for e in g.edges:
    print (e.source, e.target)

