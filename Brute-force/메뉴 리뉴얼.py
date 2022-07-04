from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        array = []
        for order in orders:
            order = sorted(order)
            array.extend(list(combinations(order,c)))
        
        count = Counter(array)
        
        if count and max(count.values()) >= 2:
            for key, value in count.items():
                if value == max(count.values()):
                    answer.append("".join(key))
                    
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))