def get_divisor_count(n):
    count = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1
    count += 1
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        check = get_divisor_count(i)
        if check % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

left = 13
right = 17
print(solution(left, right))