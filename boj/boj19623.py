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
data.sort(key =lambda x : x[1])
times = sorted(set(times))
dic = {value : index for index, value in enumerate(times)}

for i in range(len(data)):
    data[i][0] = dic[data[i][0]]
    data[i][1] = dic[data[i][1]]

print(data)
temps = []
temps.append(data[0])
for dt in data[1:]:
    #시간이 안겹칠 때
    for temp in temps:
        if max > dt[0]:
            break
        if temp[1] <= dt[0]:
            t2 = temp[2] + dt[2]
            t1 = dt[1]
            t0 = temp[0]
            #temps.remove(temp)
            temps.append([t0, t1, t2])
        else:
            if temp[2] < dt[2]:
                temps.remove(temp)
                temps.append(dt)
    temps.sort(reverse=True, key=lambda x : x[2])

    print(temps)
temps.sort(key = lambda x : x[2])
print(temps[-1][2])

#print(max)
'''
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
'''
#max = sorted(dp)[-1]
#print(max)

