def solution(number, k):
    max_num = 0
    
    for i in range(k):
        max_num = max(int(number[i]), max_num)
    start = number.index(str(max_num))
    k = k - start
    number = number[start:]
    
    min_num = 9999999
    
    while k != 0:
        for i in range(1, k + 1):
            min_num = min(int(number[i]), min_num)
        mini = number.index(str(min_num))
        k -= 1
        number = number[:mini] + number[mini+1:]
    
    return str(number)