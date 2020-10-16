from collections import deque

# class to represent a graph object:
class Graph:
    graph_dict={}
    def __init__(self, edges):
        # add edges to the undirected graph
        for(src, dest) in edges:
            if src not in self.graph_dict:
                self.graph_dict[src] = [dest]
            else:
                self.graph_dict[src].append(dest)
            
            if dest not in self.graph_dict:
                self.graph_dict[dest] = [src]
            else:
                self.graph_dict[dest].append(src)
    def show_edges(self):
        for node in self.graph_dict:
            print(node, self.graph_dict[node])
            #for neighbour in self.graph_dict[node]:
            #    print("(",node,", ",neighbour,")")

    #level order
    #Give shortest distance and shortest path of non-weighted graph
    def BFS(self, node):
        visited = {}
        level = {} #distance directory
        parent = {} #get path
        bsf_output = []
        for i in self.graph_dict:
            visited[i] = False 
            level[i] = -1
            parent[i] = None
        #empty queue
        q = deque()

        #Mark source vertex is discovered
        visited[node] = True
        level[node] = 0
        #push source vertex to Q
        q.append(node)

        while q:

            #pop the first inserted element from Q
            node = q.popleft()
            bsf_output.append(node)
            #print(node, end=' ')

            #do for to every edge
            for edg in self.graph_dict[node]:
                if not visited[edg]:
                    visited[edg] = True
                    parent[edg] = node
                    level[edg] = level[node] +1
                    q.append(edg)
        
        print("BFS")
        print(bsf_output)
        print("Level")
        print(level[5])
        print("Shortest path")
        v = 5
        path = []
        while v is not None:
            path.append(v)
            v = parent[v]
        print(path)
    
    #pre order
    def DFS(self, node):
        visited = {}
        for i in self.graph_dict:
            visited[i] = False 
        # create a stack used to do iterative DFS
        stack = deque()

        stack.append(node)
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
                
            visited[node] = True
            print(node, end=' ')

            for edg in self.graph_dict[node]:
                if not visited[edg]:
                    stack.append(edg)


if __name__ == "__main__":
    # List of graph edges as per above diagram
    edges = [
            (1,2), (1,3), (1,4), (2,5), (2,6), (5,9),
            (5,10),(4,7),(4,8),(7,11),(7,12)
            ]
    # vertex 0, 13 and 14 are single nodes
    # Set number of vertices in the graph
    N = 15
    # stores vertex is discovered or not
    discovered = [False] * N
    # create a graph from edges
    graph = Graph(edges)
    #graph.show_edges()
    graph.BFS(1)
    print("\n")
    graph.DFS(4)

    