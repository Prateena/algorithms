import sys
from collections import deque

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]

def is_valid(mat, visited, row, col):
    return row >= 0 and row < len(mat) and col >= 0 and col < len(mat) and mat[row][col] == 1 and not visited[row][col] 

def findshortestpath(mat, src, dest):
    
    x, y = src

    a, b = dest

    if not mat and len(mat) == 0 and mat[x][y] == 0 and mat[a][b] == 0:
        return -1

    (M, N) = (len(mat), len(mat[0]))

    visited = [[False for a in range(N)] for b in range(M)]

    q = deque()

    visited[x][y] = True

    q.append([x, y, 0])

    min_dist = sys.maxsize

    while q:

        (x, y, dist) = q.popleft()

        if x == a and y == b:
            min_dist = dist
            break

        for k in range(4):
            if is_valid(mat, visited, x + row[k], y + col[k]):
                visited[x + row[k]][y + col[k]] = True
                q.append([x + row[k], y + col[k], dist + 1])

    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1


if __name__ == '__main__':
 
    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]
 
    src = (0, 0)
    dest = (7, 5)

    min_dist = findshortestpath(mat, src, dest) 

    if min_dist != -1:
        print("The shortest distance is ", min_dist)
    else:
        print("Destination cannot be reached from the source")



