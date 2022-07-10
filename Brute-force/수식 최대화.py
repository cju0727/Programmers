from itertools import permutations

def operation(num1, num2, operator):
    if operator == "+":
        return str(int(num1) + int(num2))
    elif operator == "-":
        return str(int(num1) - int(num2))
    elif operator == "*":
        return str(int(num1) * int(num2))

def calculate(expression, operators):
    array = []
    tmp = ""
    for e in expression:
        if e.isdigit():
            tmp += e
        else:
            array.append(tmp)
            array.append(e)
            tmp = ""
    array.append(tmp)
    
    for o in operators:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array = stack
    
    return abs(int(array[0]))

def solution(expression):
    answer = 0
    operators = ["+", "-", "*"]
    operation_features = list(permutations(operators, 3))
    
    for operators in operation_features:
        answer = max(answer, calculate(expression, operators))
    return answer

expression = "100-200*300-500+20"
print(solution(expression))