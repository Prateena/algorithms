from collections import deque

class Graph:
    def __init__(self, edges, n):

        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
            
def iterativeDFS(graph, root_node, visited):

    stack = deque()

    stack.append(root_node)

    while stack:

        root_node = stack.pop()

        if visited[root_node]:
            continue

        visited[root_node] = True
        print(root_node, end=" ")

        adjList = graph.adjList[root_node]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not visited[u]:
                stack.append(u)

if __name__ == '__main__':
       
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]

    n = 13

    visited = [False] * n

    graph = Graph(edges, n)

    for i in range(n):
        if not visited[i]:
            iterativeDFS(graph, i, visited)





