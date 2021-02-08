import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = []
times = []

for i in range(n):
    data.append(list(map(int, input().split())))
    times.append(data[i][0])
    times.append(data[i][1])

#좌표압축
data.sort()
times = sorted(set(times))
dic = {value : index for index, value in enumerate(times)}

for i in range(len(data)):
    data[i][0] = dic[data[i][0]]
    data[i][1] = dic[data[i][1]]

dp = [0] * len(times)

for dt in data:
    if dp[dt[1]] < dt[2]:
        dp[dt[1]] = dt[2]

#print(data)
for i in range(len(data)):
    if dp[data[i][1]] > data[i][2]:
        continue 
    endTime = data[i][1]
    for j in range(i+1,len(data)):
        nStartTime = data[j][0]
        if  endTime <= nStartTime and dp[data[j][1]] < dp[endTime] + data[j][2]:
            dp[data[j][1]] = dp[endTime] + data[j][2]
           # print(endTime," ",nStartTime," ",dp[data[j][1]])
            endTime = data[j][1]
#print(dp)
max = sorted(dp)[-1]
print(max)

