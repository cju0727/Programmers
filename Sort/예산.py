def solution(d, budget):
    answer = 0
    division = sorted(d)
    
    for d in division:
        if d <= budget:
            answer += 1
            budget -= d
            
    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))