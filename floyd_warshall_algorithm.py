import math

nV = 4

INF = math.inf


def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    solution(distance)

def solution(distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")

        print(" ")

G = [[0, INF, -2, INF],
    [4, 0, 3, INF],
    [INF, INF, 0, 2],
    [INF, -1, INF, 0]
    ]

floyd_warshall(G)
