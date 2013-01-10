
def harmean(a):
  hm= float(len(a)) / sum([1.0 /x for x in a])
  return(hm)


def allsp(start):
    # initialize distances and predecessor edges
    all_edges=[] #    all_edges=g.edges # gi.edges()#    damaged= start ? end#if len(damaged) !=0:#    all_edges.discard(damaged.pop())
    for x in range(0,len(g.edges)):
        if list(g.edges)[x].weight !=0:
            all_edges.append(list(g.edges)[x])
    dist, prev , distinv= {}, {}, {}
    for v in g.nodes:
        dist[v], distinv[v], prev[v] = float('inf'), float('inf'), None
    dist[start] , distinv[start]= 0, 0
    for i in range(len(g.nodes)):   # Bellman-Ford algorithm, tweaked so that high weight = shorter distance 
        for e in all_edges: 
            if distinv[e.target] > distinv[e.source] + 1./ e.weight: #... + 1./ e.weight
                distinv[e.target] = distinv[e.source] + 1./ e.weight #... + 1./ e.weight
                dist[e.target] = dist[e.source] + e.weight 
                prev[e.target] = e
                if e.source==start or e.target ==start:
                    prev[start]=e
            if distinv[e.source] > distinv[e.target] + 1./ e.weight: #... + 1./ e.weight
                distinv[e.source] = distinv[e.target] + 1./ e.weight  #... + 1./ e.weight
                dist[e.source] = dist[e.target] + e.weight
                prev[e.source] = e
                if e.target==start or e.source ==start:
                    pass
    d,dinv=[],[]
    for v in g.nodes:
        if v!=start:
            d.append(int(dist[v]))
            dinv.append(distinv[v])
    return (d,dinv,dist,distinv)   # return the total weight of the path (distance)


[d,dinv,dist,distinv]=allsp(v11)
hm=harmean(d) # distance with the real weights (high means good)
hminv=harmean(dinv) # distance with the inverse of the weights (the one used in the algorithm to choose heavy weights)(low means good)

allhm,allhminv=[],[]
for s in g.nodes:
    [d,dinv,dist,distinv]=allsp(s)
    allhm.append(harmean(d))
    allhminv.append(harmean(dinv))

hm=harmean(allhm) # distance with the real weights (high means good)
hminv=harmean(allhminv) 

#
[d,dinv,dist,distinv]=allsp(v11)
hm=harmean(d) # distance with the real weights (high means good)
hminv=harmean(dinv) # distance with the inverse of the weights (the one used in the algorithm to choose heavy weights)(low means good)


>>>print ([list(g.edges)[x].weight for x in range(0,len(g.edges))])