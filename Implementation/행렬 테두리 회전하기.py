def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    num = 1
    
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = num
            num += 1
    
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]
        mini = tmp
        
        for i in range(x1, x2):
            prev = matrix[i+1][y1]
            matrix[i][y1] = prev
            mini = min(mini, prev)
        
        for i in range(y1, y2):
            prev = matrix[x2][i+1]
            matrix[x2][i] = prev
            mini = min(mini, prev)
        
        for i in range(x2, x1, -1):
            prev = matrix[i-1][y2]
            matrix[i][y2] = prev
            mini = min(mini, prev)
        
        for i in range(y2, y1, -1):
            prev = matrix[x1][i-1]
            matrix[x1][i] = prev
            mini = min(mini, prev)
            
        matrix[x1][y1 + 1] = tmp
        answer.append(mini)
        
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))