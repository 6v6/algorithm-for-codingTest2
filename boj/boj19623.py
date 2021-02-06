import sys
from collections import deque
input = sys.stdin.readline

def dfs(data, i, dp, numbers):
    global max
    if dp[i] < numbers:
        dp[i] = numbers
    else:
        return
    endTime = data[i][1]

    for j in range(i+1, len(data)):
        nStartTime = data[j][0]
        if  endTime <= nStartTime:
            newNum = numbers + data[j][2]
            dfs(data, j, dp, newNum)


n = int(input())
data = []
dp = [0] * n

for i in range(n):
    s, e, num  = list(map(int, input().split()))
    data.append([s,e,num])
data = sorted(data)
#print(data)

for i in range(n):
    dfs(data, i, dp, data[i][2])

max = sorted(dp)[-1]
print(max)

