def solution(board, moves):
    answer = 0
    check = []
    
    for m in moves:
        for column in board:
            if column[m-1] != 0:
                check.append(column[m-1])
                if len(check) > 1 and check[-2] == check[-1]:
                    check.pop()
                    check.pop()
                    answer += 2
                column[m-1] = 0
                break
        
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))