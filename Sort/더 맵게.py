def solution(scoville, K):
    answer = 0
    new_food = 0
    scoville.sort(reverse = True)
    while scoville[-1] < K:
        new_food = scoville.pop() + (2 * scoville.pop())
        answer += 1
        scoville.append(new_food)
        scoville.sort(reverse = True)
    
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))