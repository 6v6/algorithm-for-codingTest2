from collections import deque


n = int(input())
graph = [[] for _ in range(n+1)]
parent = [ 0 for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append(1)

while q:
    now = q.popleft()
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            parent[i] = now
            q.append(i)


for i in parent[2:]:
    print(i)
