def check(mid, stones, k):
    count = 0
    for s in stones:
        if s < mid:
            count += 1
            if count >= k:
                return False
        else:
            count = 0

    return True


def solution(stones, k):
    answer = 0
    left = 1
    right = sorted(stones)[-1]
    while(left <= right):
        mid = (left + right)//2
        if check(mid, stones, k):
            #print(mid)
            if answer < mid:
                answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
