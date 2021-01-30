import sys
input = sys.stdin.readline

n, h = map(int, input().split())
bottom = [0] * (h+1)
top = [0] * (h+1)
for i in range(n):
    if i % 2 == 0:
        bottom[int(input())] += 1
    else:
        top[h-int(input())+1] += 1

for x in range(h-1, 0, -1):
    bottom[x] += bottom[x+1]

for x in range(2, h+1):
    top[x] += top[x-1]

answer = [0] * (h+1)

for i in range(1, h+1):
    answer[i] = top[i] + bottom[i]


results = answer[1:]
result = min(results)
print(result, results.count(result))