from itertools import permutations
def check(cl, banned_id):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(cl[i]):
            return False
        else:
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == "*" or banned_id[i][j] == cl[i][j]:
                    continue
                elif banned_id[i][j] != cl[i][j]:
                    return False
    return True
                    
def solution(user_id, banned_id):
    answer = 0
    answerList = []
    canList = list(permutations(user_id, len(banned_id)))
    for cl in canList:
        if check(cl, banned_id):
            cl = set(cl)
            if cl not in answerList:
                answerList.append(cl)
    answer = len(answerList)           
    return answer