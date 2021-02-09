import sys
import heapq

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort()

count = 1
q = []
heapq.heappush(q, data[0][1])

for d in data[1:]:
    #가장 빨리 나가는 시간보다 현재 시작시간이 더 빠르면
    if q[0] > d[0]:
        count += 1
    else:
        heapq.heappop(q)
    heapq.heappush(q, d[1])

print(count)