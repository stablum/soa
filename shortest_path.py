def shortest_path(start, end):
    # initialize distances and predecessor edges
    all_edges=g.edges # gi.edges()
    damaged= start ? end
    if len(damaged) !=0:
        all_edges.discard(damaged.pop())
    dist, prev = {}, {}
    sp_nodes=set([])
    for v in g.nodes:
        dist[v], prev[v] = float('inf'), None
    dist[start] = 0
    for i in range(len(g.nodes)):   # Bellman-Ford algorithm, tweaked so that high weight = faster 
        for e in all_edges: # TODO: exclude from the count the original AB
            if dist[e.target] > dist[e.source] + 1/e.weight:
                dist[e.target] = dist[e.source] + 1/e.weight
                prev[e.target] = e
                print (e.target, e.source)
    for v in g.nodes:# color all the nodes and edges as RGB 200, 200, 200
        v.color = color(200, 200, 200)
    for e in g.edges:
        e.color = color(200, 200, 200)
    if dist[end] < float('inf'):    # highlight a shortest path with the green color (if one exists)
        e = prev[end]
        end.color = green
        while e != None: #while
            e.color = green
            e.source.color = green
            e = prev[e.source]
            sp_nodes.add(e)            #ee=prev[e.target] #mik     #sp_nodes.add(ee) #mik
    return (dist[end], sp_nodes)   # return the total weight of the path (distance)

if e.source == start e.target==start
    firstlaste.appen(e)
    
    #\def get_equal(in_set, in_element):
   for element in in_set:
       if element == in_element:
           return element
   return None 