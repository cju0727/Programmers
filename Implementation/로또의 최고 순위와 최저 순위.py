def lotto_count(count):
    if count == 6:
        answer = 1
    elif count == 5:
        answer = 2
    elif count == 4:
        answer = 3
    elif count == 3:
        answer = 4
    elif count == 2:
        answer = 5
    else:
        answer = 6
        
    return answer

def solution(lottos, win_nums):
    answer = []
    zero = 0
    count = 0
    
    for l in lottos:
        if l == 0:
            zero += 1
        if l in win_nums:
            count += 1
            
    answer.append(lotto_count(count + zero))
    answer.append(lotto_count(count))
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))