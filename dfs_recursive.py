class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
 
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
def DFS(graph, v, visited):
 
    visited[v] = True           
    print(v, end=' ')               
 
    for u in graph.adjList[v]:
        if not visited[u]:
            DFS(graph, u, visited)
 
 
if __name__ == '__main__':
 
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    n = 13
 
    graph = Graph(edges, n)
 
    visited = [False] * n
 
    for i in range(n):
        if not visited[i]:
            DFS(graph, i, visited)