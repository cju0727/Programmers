def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    answer = n - len(new_lost)
    
    for l in new_lost:
        if l - 1 in new_reserve:
            answer += 1
            new_reserve.remove(l - 1)
        elif l + 1 in new_reserve:
            answer += 1
            new_reserve.remove(l + 1)
            
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

print(solution(n, lost, reserve))