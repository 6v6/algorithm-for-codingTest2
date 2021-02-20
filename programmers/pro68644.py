from itertools import combinations


def solution(numbers):
    answer = []
    clist = list(combinations(numbers, 2))
    z = 0
    for i in clist:
        x = i[0]
        y = i[1]
        z = x+y
        if z not in answer:
            answer.append(z)
    answer.sort()
    return answer
