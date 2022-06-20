import re

def solution(s):
    answer = 0
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(10):
        al = re.escape(alpha[i])
        nu = re.escape(number[i])
        s = re.sub(al, nu, s)
    answer = int(s)
    
    return answer

s = "one4seveneight"
print(solution(s))