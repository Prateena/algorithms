import math
from heapq import heappop, heappush

class Edge:
    def __init__(self, vertex, weight = 0):
        self.vertex = vertex
        self.weight = weight

    def __lt__(self, other):
        self.weight < other.weight

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))
        
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)

def findshortestpaths(graph, source, n):

    priority_queue = []

    heappush(priority_queue, Edge(source))
    
    dist = [math.inf] * n

    dist[source] = 0

    done = [False] * n
    done[source] = True
 
    prev = [-1] * n
 
    while priority_queue:
 
        node = heappop(priority_queue)
        u = node.vertex         
 
        for (v, weight) in graph.adjList[u]:
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(priority_queue, Edge(v, dist[v]))
 
        done[u] = True
 
    route = []
    for i in range(n):
        if i != source and dist[i] != math.inf:
            get_route(prev, i, route)
            print(f'Path ({source} —> {i}): Minimum cost = {dist[i]}, Route = {route}')
            route.clear()

if __name__ == '__main__':
    
    edges = [(0, 1, 7),(1, 2, 8),(2, 3, 9)]

    n = 4

    graph = Graph(edges,n)
    for i in range(n):
        findshortestpaths(graph, i, n)
