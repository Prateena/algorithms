from collections import deque
 
class Graph:
    def __init__(self, edges, n):
 
        self.adjList = [[] for _ in range(n)]
 
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
def recursiveBFS(graph, q, visited):
 
    if not q:
        return
 
    v = q.popleft()
    print(v, end=' ')
 
    for u in graph.adjList[v]:
        if not visited[u]:
            visited[u] = True
            q.append(u)
 
    recursiveBFS(graph, q, visited)
 
 
if __name__ == '__main__':
 
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
    ]
 
    n = 15
 
    graph = Graph(edges, n)
 
    visited = [False] * n
 
    q = deque()
 
    for i in range(n):
        if not visited[i]:
            visited[i] = True
 
            q.append(i)
 
            recursiveBFS(graph, q, visited)