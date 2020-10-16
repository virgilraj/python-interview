
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
    
    def __str__(self):
        return str(self.id) + ' adjacent : ' + str([x.id for x in self.adjacent])
    
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    def get_connections(self):
        return self.adjacent.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    
    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    
    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
    
    def get_vertices(self):
        return self.vert_dict.keys()
        
    
if __name__ == "__main__":
    g = Graph()

    g.add_vertex('a')
    #g.add_vertex('b')

    g.add_edge('a', 'b', 3)
    g.add_edge('a', 'c', 1)
    g.add_edge('c', 'b', 1)
    #g.add_edge('b', 'd', 2)
    #g.add_edge('c', 'f', 3)
    #g.add_edge('e', 'g', 2)

    #for v in g:
    #    print(v)
    
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            weight = v.get_weight(w)
            print(vid, wid, weight)

