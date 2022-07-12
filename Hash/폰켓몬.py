def solution(nums):
    answer = 0
    target = len(nums)//2
    nums = set(nums)
    
    for n in nums:
        if answer < target:
            answer += 1
            
    return answer

nums = [3, 1, 2, 3]
print(solution(nums))