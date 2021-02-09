def solution(m, n, puddles):
    answer = 0
    map = [[0] * m for _ in range(n)]
    for puddle in puddles:
        x = puddle[1]-1
        y = puddle[0]-1
        map[x][y] = -1
    
    map[0][0] = 1
    print(map)
    for i in range(n):
        for j in range(m):
            right = 0
            down = 0
            if map[i][j] == -1: continue
            if j > 0 and map[i][j-1] != -1:
                right = map[i][j-1]
            if i > 0 and map[i-1][j] != -1:
                down = map[i-1][j]
            map[i][j] += right + down
    answer = map[n-1][m-1] % 1000000007
    return answer