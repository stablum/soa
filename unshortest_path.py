# the following should be copy pasted
# problem: currently this algorythm favour shortest path with low weight rather than high
# solution (with bugs to be fixed): favour high  weight by adding the opposite of the weight 1./ e.weight
# this way: high weight = good easy connection
# buggy: does not seem to behave well, hilights only last steps of the path. try it out...

def unshortest_path(start, end):
    # initialize distances and predecessor edges
    all_edges=g.edges # gi.edges()#    damaged= start ? end#if len(damaged) !=0:#    all_edges.discard(damaged.pop())
    dist, prev = {}, {}
    for v in g.nodes:
        dist[v], prev[v] = float('inf'), None
    dist[start] = 0
    for i in range(len(g.nodes)+1):   # Bellman-Ford algorithm, tweaked so that high weight = faster 
        for e in all_edges: # TODO: exclude from the count the original AB
            if dist[e.target] > dist[e.source] + e.weight: #... + 1./ e.weight
                dist[e.target] = dist[e.source] + e.weight #... + 1./ e.weight
                prev[e.target] = e
                print ( i, e.source, e.target, e.weight, '         ', e)
                if e.source==start or e.target ==start:
                    print ('!!!!!!', e.source,e.target, prev[e.source], prev[e.target])
                    prev[start]=e
            if dist[e.source] > dist[e.target] + e.weight: #... + 1./ e.weight
                dist[e.source] = dist[e.target] + e.weight  #... + 1./ e.weight
                prev[e.source] = e
                print ( i, e.source, e.target, e.weight, '         ', e)
                if e.target==start or e.source ==start:
                    print ('!!!!!!', e.source, e.target, prev[e.source],prev[e.target])
    print('prev(start) + prev(end)', prev[start], prev[end])
    for v in g.nodes:# color all the nodes and edges as RGB 200, 200, 200
        v.color = color(200, 200, 200)
    for e in g.edges:
        e.color = color(200, 200, 200)
    return (dist[end], prev, dist)   # return the total weight of the path (distance)
 
[a,prev,dist]=unshortest_path(v33, v67)

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
            if e ==None:
                break


ee=[]; squeak=0;
e= prev[v67]
for i in range(1,10):
    if ee!= None:
        ee=prev[e.source]
        e.source.color=green
        if ee.source== e.source:
            print ("1",e.source, e.target, e)
            ee=prev[e.target]
            e.target.color=green
        else:
            print ("2",e.source, e.target, e)
        e=ee
        e.color=green
    else:
        True
    if squeak==1 :
        break
    if ee.source==v33:
        squeak=1

                
unshortest_path(v33, v11)
