#크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    stack = []
    n = len(board[0])
    for i in moves:
        for j in range(n):
            if board[j][i-1] != 0:
                if stack:
                    if stack[-1] != board[j][i-1]:
                        stack.append(board[j][i-1])
                    else:
                        answer += 2
                        stack.pop()
                else:
                    stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
    return answer