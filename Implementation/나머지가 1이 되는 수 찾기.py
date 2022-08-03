def solution(n):
    answer = 0
    target = n - 1

    for i in range(2, target//2 + 1):
        if target % i == 0:
            answer = i
            break

    if answer == 0:
        answer = target

    return answer


n = 12
print(solution(n))
