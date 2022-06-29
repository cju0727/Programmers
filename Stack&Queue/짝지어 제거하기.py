def solution(s):
    answer = -1
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    answer = 1 if not stack else 0
    return answer

s = "baabaa"
print(solution(s))