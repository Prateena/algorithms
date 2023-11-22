
from collections import deque

class Graph:
    def __init__(self, edges, n):

        self.Adjlist = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.Adjlist[src].append(dest)
            self.Adjlist[dest].append(src)

def BFS(graph, root_node, visited):

    q = deque()

    visited[root_node] = True

    q.append(root_node)

    while q:
        root_node = q.popleft()
        print(root_node, end=" ")

        for child in graph.Adjlist[root_node]:
            if not visited[child]:
                visited[child] = True
                q.append(child)

if __name__ == '__main__':

    # edges = [(2,3),(2,4),(2,5),(3,8),(3,10),(4,9),(5,11),(8,12)]

    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12), (8, 13)
    ]
 
    n = 16
 
    graph = Graph(edges, n)

    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            BFS(graph, i, visited)



