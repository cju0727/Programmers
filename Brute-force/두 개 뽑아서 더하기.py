from itertools import combinations

def solution(numbers):
    answer = []
    tmp = 0
    com = combinations(numbers, 2)
    for a, b in list(com):
        tmp = a+b
        if tmp not in answer:
            answer.append(tmp)
            answer.sort()
        
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))