def solution(numbers, target):
    answer = 0
    result = [0]
    for n in numbers:
        tmp = []
        for r in result:
            tmp.append(r-n)
            tmp.append(r+n)
        result = tmp
        answer = result.count(target)

    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))