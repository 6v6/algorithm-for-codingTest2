def solution(triangle):
    answer = 0
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            if triangle[i+1][j] < triangle[i+1][j+1]:
                triangle[i][j] += triangle[i+1][j+1]
            else:
                triangle[i][j] += triangle[i+1][j]
    return triangle[0][0]
