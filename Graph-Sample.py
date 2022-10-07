from collections import deque
class Graph:
    def __init__(self, V, E, is_directed=False):
        self.Vertices = V
        self.Edges = E
        self.isDirected = is_directed
        self.AdjacencyList = self.adjacency_list(V, E, is_directed)
        self.AdjacencyMat = self.adjacency_mat(V, E, is_directed)

    def adjacency_list(self, V, E, is_directed):
        adj_list = {node: [] for node in V}        
        for e in E:
            node1, node2 = e[0], e[1]
            adj_list[node1].append(node2)
            if not is_directed:
                adj_list[node2].append(node1)
        return adj_list

    def adjacency_mat(self, V, E, is_directed):
        adj_mat = [[0 for _ in V] for _ in V]
        # .....
        return adj_mat

    def DFS(self, start, visited=set()):
        if start not in visited:
            visited.add(start)
            print(start, end = ' ') # visit
        for adj in self.AdjacencyList[start]:
            if adj not in visited:
                self.DFS(adj, visited)       

    def BFS(self, start, visited=set()):
        Q = deque()
        # ......
        pass

if __name__ == '__main__':
    V = ['A','B','C','D','E','F']
    E = [['A','B'],['A','C'],['B','C'],['B','D'],
         ['B','E'],['C','D'],['D','E'],['E','F']]
    G = Graph(V, E)
    print(G.AdjacencyList)
    print(G.AdjacencyMat)
    # expected output: 
    # [[0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0]]
    G.DFS('A')