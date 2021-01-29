import sys
import collections
from collections import deque

INF = int(1e9)
#가로크기m, 세로크기n
m, n = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

distance = [[INF]*m for _ in range(n)]

distance[0][0] = 0
q = deque()
q.append([0, 0])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            cost = distance[x][y] + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                q.append([nx, ny])

print(distance[n-1][m-1])
