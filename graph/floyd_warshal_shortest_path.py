'''Input:
       graph[][] = { {0,   5,  INF, 10},
                    {INF,  0,  3,  INF},
                    {INF, INF, 0,   1},
                    {INF, INF, INF, 0} }
which represents the following graph
             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3       
Note that the value of graph[i][j] is 0 if i is equal to j 
And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.

Output:
Shortest distance matrix
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0 
'''

def floydWarshall(graph):
    n = len(graph)
    #Copy to shortest path
    dist = [[0 for x in range(n)] for y in range(n) ]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    
    #Find all pairs shortest path by trying all possible paths
    """ Add all vertices one by one to the set of intermediate 
     vertices. 
     ---> Before start of an iteration, we have shortest distances 
     between all pairs of vertices such that the shortest 
     distances consider only the vertices in the set  
    {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of a iteration, vertex no. k is 
     added to the set of intermediate vertices and the  
    set becomes {0, 1, 2, .. k} 
    """
    for k in range(n): #Try all intermediate nodes\
        for i in range(n): #Try for all possible starting position
            for j in range(n): #Try for all possible ending position
                #SKIP if K is unreachable from i or j is unreachable from k
                if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                    continue
                else:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])    
    
    #Check for negative edge weight cycle
    for i in range(n):
        if dist[i][i] < 0:
            print("Negative edge weight cycle is present\n")
            return
    
    #Print Shortest Path Graph
    print(dist)
    #for i in range(n):
    #    for j in range(n):
    #        if dist[i][j] == float('inf'):
    #            print("%7s" %("INF"))
    #        else:
    #            print("%7s" %(dist[i][j]))


# Driver program to test the above program 
# Let us create the following weighted graph 
""" 
            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
            3           """
if __name__ == "__main__":
    INF = float('inf')
    g=[
        [0,5,INF, 10],
        [INF,0,3, INF],
        [INF,INF,0, 1],
        [INF,INF,INF, 0]
    ]
    floydWarshall(g)