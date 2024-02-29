def solution(board, moves):
    answer = 0
    n = len(board)
    board_T = list(map(list, zip(*board)))
    stack = []
    for i in moves:
        for j in range(n):
            if board_T[i-1][j] > 0:

                if stack:
                    if stack[-1] == board_T[i-1][j]:

                        stack.pop()
                        answer += 2
                        board_T[i - 1][j] = 0
                        break
                stack += [board_T[i-1][j]]
                board_T[i - 1][j] = 0
                break

    return answer