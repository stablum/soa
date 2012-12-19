def shortest_path(start, end):
    # initialize distances and predecessor edges
    dist, prev = {}, {}
    for v in g.nodes:
        dist[v], prev[v] = float('inf'), None
    dist[start] = 0
    for i in range(len(g.nodes)):   # Bellman-Ford algorithm
        for e in g.edges:
            if dist[e.target] > dist[e.source] + 1/e.weight:
                dist[e.target] = dist[e.source] + 1/e.weight
                prev[e.target] = e
    for v in g.nodes:# color all the nodes and edges as RGB 200, 200, 200
        v.color = color(200, 200, 200)
    for e in g.edges:
        e.color = color(200, 200, 200)
    if dist[end] < float('inf'):    # highlight a shortest path with the green color (if one exists)
        e = prev[end]
        end.color = green
        while e != None:
            e.color = green
            e.source.color = green
            e = prev[e.source]
    return dist[end]    # return the total weight of the path (distance)