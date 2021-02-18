import sys
from copy import deepcopy
from collections import deque

max_value = 0


def move(board, n):
    temp = [[0]*n for _ in range(n)]
    for x in range(n):
        flag = 0
        target = -1
        for y in range(n):
            if board[y][x] == 0:
                continue

            if flag == 1 and board[y][x] == temp[target][x]:
                temp[target][x] *= 2
                flag = 0
            else:
                target += 1
                temp[target][x] = board[y][x]
                flag = 1

        target += 1
        for i in range(target, n):
            temp[target][x] = 0

    return temp


def rotate(board, n):
    temp = [[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            temp[y][x] = board[n-x-1][y]
    return temp


def dfs(graph, n, depth):
    if depth == 5:
        for i in range(n):
            global max_value
            max_value = max(max_value, max(graph[i]))
        return

    for i in range(4):
        next = deepcopy(graph)
        next = move(next, n)
        dfs(next, n, depth + 1)
        graph = rotate(graph, n)


input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
dfs(graph, n, 0)
print(max_value)
