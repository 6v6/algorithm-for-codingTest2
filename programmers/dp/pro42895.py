def solution(N, number):
    answer = -1
    data = []
    if number == N:
        return 1
    data.append([])
    data.append([N])
    count = 0
    for i in range(2, 9):
        temp = []
        for j in range(1, i):
            for p in data[j]:
                for q in data[i-j]:
                    temp.append(p + q)
                    temp.append(p - q)
                    temp.append(p * q)
                    if q != 0:
                        temp.append(p // q)
        temp.append(int(str(N)*i))
        data.append(set(temp))
        if number in set(temp):
            return i
    return answer
