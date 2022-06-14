def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2 + 1):
        word = ""
        prev = s[:step]
        count = 1
        
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                word += str(count) + prev if count >= 2 else prev
                prev = s[i:i+step]
                count = 1
            
        word += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(word))
        
    return answer

s = "aabbaccc"
print(solution(s))
s = "ababcdcdababcdcd"
print(solution(s))
s = "abcabcdede"
print(solution(s))
s = "abcabcabcabcdededededede"
print(solution(s))
s = "xababcdcdababcdcd"
print(solution(s))