import gi

def harmean(a):
    
    # removing values 0 in the list 'a'
    a_filt = filter(lambda x: x != 0, a)
    
    a_no_inf = [ 99999 if x > 99999 else x for x in a_filt ]

    # calculating harmonic mean
    s = sum([1.0 /x for x in a_no_inf])
    
    if s == 0:
        raise Exception("harmean: sum is 0; a="+str(a)+",a_filt="+str(a_filt)+",a_no_inf="+str(a_no_inf))
    
    hm = float(len(a)) / float(s)
    return hm

def allsp(start):
    # initialize distances and predecessor edges
    all_edges=gi.alive_edges() # gi.edges()#    damaged= start ? end#if len(damaged) !=0:#    all_edges.discard(damaged.pop())
    dist, prev , distinv= {}, {}, {}
    for v in gi.nodes():
        dist[v], distinv[v], prev[v] = float('inf'), float('inf'), None
    dist[start] , distinv[start]= 0, 0
    for i in range(len(gi.nodes())):   # Bellman-Ford algorithm, tweaked so that high weight = shorter distance 
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
    for v in gi.nodes():
        if v!=start:
            d.append((dist[v])) #int
            dinv.append(distinv[v])
    return d,dinv,dist,distinv   # return the total weight of the path (distance)


def getpl():
    allhm,allhminv,hm,hminv=[],[],[],[]
    for s in gi.nodes():
        [d,dinv,dist,distinv]=allsp(s)
        allhm.append(harmean(d))
        allhminv.append(harmean(dinv))
    hm=float(harmean(allhm)) # distance with the real weights (high means good)
    hminv=harmean(allhminv) 
    return hminv

