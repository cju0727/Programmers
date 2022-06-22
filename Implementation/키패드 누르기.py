def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"
    keypad = {'*': [4, 1], 0: [4, 2], "#": [4, 3]}
    for i in range(1, 10):
        keypad[i] = [i//3 + 1, i%3] if i%3 else [i//3, 3]
    
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += "L"
            left = numbers[i]
        elif numbers[i] in [3, 6, 9]:
            answer += "R"
            right = numbers[i]
        else:
            if abs(keypad[numbers[i]][0] - keypad[left][0]) + \
            abs(keypad[numbers[i]][1] - keypad[left][1]) == \
            abs(keypad[numbers[i]][0] - keypad[right][0]) + \
            abs(keypad[numbers[i]][1] - keypad[right][1]):
                if hand == "right":
                    answer += "R"
                    right = numbers[i]
                else:
                    answer += "L"
                    left = numbers[i]
            
            elif abs(keypad[numbers[i]][0] - keypad[left][0]) + \
            abs(keypad[numbers[i]][1] - keypad[left][1]) < \
            abs(keypad[numbers[i]][0] - keypad[right][0]) + \
            abs(keypad[numbers[i]][1] - keypad[right][1]):
                answer += "L"
                left = numbers[i]
            
            else:
                answer += "R"
                right = numbers[i]
            
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))