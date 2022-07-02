import math
from itertools import combinations

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
        

def solution(nums):
    answer = 0
    for a, b, c in combinations(nums, 3):
        if is_prime_number(a + b + c):
            answer += 1
    
    return answer

nums = [1,2,3,4]
print(solution(nums))