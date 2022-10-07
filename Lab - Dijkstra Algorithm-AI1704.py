from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

if __name__ == "__main__":
    g = Graph(8)
    g.add_edge(0, 1, 3)
    g.add_edge(0, 6, 6)
    g.add_edge(1, 6, 10)
    g.add_edge(1, 7, 12)
    g.add_edge(1, 2, 7)
    g.add_edge(2, 3, 9)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 4, 8)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 13)
    g.add_edge(4, 7, 2)
    g.add_edge(6, 7, 1)
    
    

    D = dijkstra(g, 0)
    for vertex in range(len(D)):
        print(" kc tu vecto0 from vect",vertex,"is", D[vertex])