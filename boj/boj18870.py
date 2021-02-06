import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data2 = sorted(set(data))
dic = {value : index for index, value in enumerate(data2)}

for i in data:
    print(dic[i], end = " ")