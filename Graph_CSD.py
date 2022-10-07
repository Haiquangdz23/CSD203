from collections import deque
class Graph:
    def __init__(self, V, E, is_directed = False):
        self.Vertices = V
        self.Edges = E
        self.isDirected = is_directed
        
    def adjacency_list(self):
        adj_list = {node: [] for node in self.Vertices}
        for edge in self.Edges:
            node1, node2 = edge[0], edge[1]
            adj_list[node1].append(node2)
            if not self.isDirected:
                adj_list[node2].append(node1)
            
        return(adj_list)
    
    def DFSalgorithm(self, adjlist, v, visited = set()):
        if v not in visited:
            print(v, end = ' ')
            visited.add(v) 
            for w in adjlist[v]:
                if w not in visited:
                    self.DFSalgorithm(adjlist, w, visited)
    
    def DFS(self, start):
        if start not in self.Vertices:
            return
        adj_list = self.adjacency_list()
        self.DFSalgorithm(adj_list, start)
        
    def BFS(self, start, visited = set()):
        if start not in self.Vertices:
            return
        adj_list = self.adjacency_list()
        Q = deque()
        Q.append(start)
        while len(Q) != 0     :
            v = Q.popleft()
            if v not in visited:
                print(v, end = ' ')
                visited.add(v)
                
                for w in adj_list[v]:
                    if w not in visited:
                        Q.append(w)
                        
    def adjacency_matrix(self):
        adjacency_matrix = [[0 for _ in self.Vertices] for _ in self.Vertices]
        for e in self.Edges:
            N1, N2 = e[0], e[1]
            A = self.Vertices.index(N1)
            B = self.Vertices.index(N2)
            adjacency_matrix[A][B] = 1
            adjacency_matrix[B][A] = 1
        return adjacency_matrix
    
                
            
    
        
if __name__ == '__main__':
    V = ['A','B','C','D','E','F']
    E = [['A','B'],['A','C'],['B','C'],['B','D'],['B','E'],['C','D'],['D','E'],['E','F']]
    G = Graph(V, E)
    for i in G.adjacency_list().items():
        print(i)
    print(G.adjacency_list())
    G.DFS('D')
    print('\n-----------')
    G.BFS('E')
    print('\n-----------')
    print(G.adjacency_matrix())
    
    