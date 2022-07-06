from collections import Counter

def solution(str1, str2):
    answer = 0
    first  = []
    second = []
    
    for i in range(len(str1)):
        if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2:
            first.append(str1[i:i+2].upper())
    
    for j in range(len(str2)):
        if str2[j:j+2].isalpha() and len(str2[j:j+2]) == 2:
            second.append(str2[j:j+2].upper())
    
    intersection = list((Counter(first) & Counter(second)).elements())
    union = list((Counter(first) | Counter(second)).elements())
    
    if len(union) == 0:
        answer = 1
    else:
        answer = len(intersection) / len(union)
        
    return int(answer * 65536)

str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2))