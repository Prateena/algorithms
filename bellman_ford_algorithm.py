class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edges(self, s, d, w):
        self.graph.append([s, d, w])

    def print_output(self, dist):
        for i in range(self.V):
            print("{} -> -> {}".format(i, dist[i]))

    def bellman_ford(self, src):

        dist = [float("INF")] * self.V

        dist[src] = 0

        for _ in range(self.V -1):
            for s, d, w in self.graph:
                if dist[s] != float("INF") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float("INF") and dist[s] + w < dist[d]:
                dist[d] = dist[s] + w

        self.print_output(dist)

g = Graph(5)
g.add_edges(0, 1, 5)
g.add_edges(0, 2, 4)
g.add_edges(1, 3, 3)
g.add_edges(2, 1, 6)
g.add_edges(3, 2, 2)

g.bellman_ford(0)